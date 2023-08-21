import torch
import math
MAX_RESOLUTION=8192

class NoisyLatentPerlin:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            "width": ("INT", {"default": 1024, "min": 8, "max": MAX_RESOLUTION, "step": 8}),
            "height": ("INT", {"default": 1024, "min": 8, "max": MAX_RESOLUTION, "step": 8}),
            "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "create_noisy_latents_perlin"
    CATEGORY = "latent/noise"

    # found at https://gist.github.com/vadimkantorov/ac1b097753f217c5c11bc2ff396e0a57
    # which was ported from https://github.com/pvigier/perlin-numpy/blob/master/perlin2d.py
    def rand_perlin_2d(self, shape, res, fade = lambda t: 6*t**5 - 15*t**4 + 10*t**3):
        delta = (res[0] / shape[0], res[1] / shape[1])
        d = (shape[0] // res[0], shape[1] // res[1])
        
        grid = torch.stack(torch.meshgrid(torch.arange(0, res[0], delta[0]), torch.arange(0, res[1], delta[1])), dim = -1) % 1
        angles = 2*math.pi*torch.rand(res[0]+1, res[1]+1)
        gradients = torch.stack((torch.cos(angles), torch.sin(angles)), dim = -1)
        
        tile_grads = lambda slice1, slice2: gradients[slice1[0]:slice1[1], slice2[0]:slice2[1]].repeat_interleave(d[0], 0).repeat_interleave(d[1], 1)
        dot = lambda grad, shift: (torch.stack((grid[:shape[0],:shape[1],0] + shift[0], grid[:shape[0],:shape[1], 1] + shift[1]  ), dim = -1) * grad[:shape[0], :shape[1]]).sum(dim = -1)
        
        n00 = dot(tile_grads([0, -1], [0, -1]), [0,  0])
        n10 = dot(tile_grads([1, None], [0, -1]), [-1, 0])
        n01 = dot(tile_grads([0, -1],[1, None]), [0, -1])
        n11 = dot(tile_grads([1, None], [1, None]), [-1,-1])
        t = fade(grid[:shape[0], :shape[1]])
        return math.sqrt(2) * torch.lerp(torch.lerp(n00, n10, t[..., 0]), torch.lerp(n01, n11, t[..., 0]), t[..., 1])

    def rand_perlin_2d_octaves(self, shape, res, octaves=1, persistence=0.5):
        noise = torch.zeros(shape)
        frequency = 1
        amplitude = 1
        for _ in range(octaves):
            noise += amplitude * self.rand_perlin_2d(shape, (frequency*res[0], frequency*res[1]))
            frequency *= 2
            amplitude *= persistence
        noise = (torch.sin(torch.remainder(noise*1000000,83))+1)/2
        return noise
    
    def scale_tensor(self, x):
        min_value = x.min()
        max_value = x.max()
        x = (x - min_value) / (max_value - min_value)
        return x

    def create_noisy_latents_perlin(self, seed, width, height, batch_size):
        torch.manual_seed(seed)
        noise = torch.zeros((batch_size, 4, height // 8, width // 8), dtype=torch.float32, device="cpu").cpu()
        for i in range(batch_size):
            for j in range(4):
                noise_values = self.rand_perlin_2d_octaves((height // 8, width // 8), (1,1), 1, 1)
                result = (2/3)*torch.erfinv(2 * noise_values - 1) * (2 ** 0.5)
                result = torch.clamp(result,-5,5)
                noise[i, j, :, :] = result
        return ({"samples": noise},)
    
NODE_CLASS_MAPPINGS = {
    "NoisyLatentPerlin": NoisyLatentPerlin,
}
