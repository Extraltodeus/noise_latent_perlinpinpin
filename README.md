# noise_latent_perlinpinpin
This allows to create latent spaces filled with perlin-based noise that can actually be used by the samplers.

# Update!
I simplified the algorith to now be able to support all resolutions (you should keep the same aspect ratio if you're upscaling however).
It is also much more simple to use as well as it will have no artifacts.

The simple trick to break the perlin pattern is now the following line:

    noise = torch.remainder(torch.abs(noise)*1000000,11)/11

This just detroys the smooth pattern while keeping it predictable at all scales.


# installation:
Just drop the .py file in your custom nodes folder or download the repository as zip and put it in the custom nodes folder.

You will also need BlenderNeko noise related nodes to use this and the workflow:

https://github.com/BlenderNeko/ComfyUI_Noise

[I highly recommend to use city96 latent upscaler in order to upscale the latent in the middle of the generation if you want to use this node for better upscales!](https://github.com/city96/SD-Latent-Upscaler)

A workflow using his node is within the house picture at the end of the readme.

# known limitation:
- You should keep the exact same aspect ratios if you want to upscale or the patterns will not match. ⚠⚠⚠⚠⚠⚠

# Use

I've included a workflow with notes in it to give you the basics but this is uncharted territory.

Euler works good with normal noise, dpmpp2m with karras is pretty nice.

![image](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/22b5e919-8d05-491b-af0c-7c62a78eb6d7)

Now you can reinject the same noise pattern after an upscale and get more coherent results.

# Example / Idea

This Perlin Merlin Rabbit has been made with SDXL using the perlin based noise.

The workflow has been noisy perlin injection (defaults settings from the shared node) -> SDXL Base (15 steps) -> VAE decode -> lanczos resize (x1.5) -> VAE encode -> same seed noisy perlin injection (but 1.5x bigger) -> SDXL refiner (5 steps)

The lanczos resize nodes are [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos.py) and [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos_to_res.py)

![00296UI_00001_](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/cd06e1e8-e5bd-461a-8e54-f114a83afdf9)


Comfy workflow included in this image. It has been upscaled x2 mid generation using SD1.5 (realistic vision 30). BNK_Noise generator is present yet disconnected (delete it if you don't have it then), it uses [city96 latent upscaler](https://github.com/city96/SD-Latent-Upscaler):

![00049UI_00001_](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/823e945f-a00b-4101-87c2-4fa776004250)

# Another comparison:

Upscaled with perlin-based noise:

![261039117-ce59f1cb-f1d7-42ad-931c-996e6e952eba](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/65e1ed88-89fc-4df2-9301-09468b61122a)

Here the noise that has been injected in the latent space after the upscale is the usual noise:

![261060650-c56fd782-6e24-49c6-946d-53c199d7272d](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/accf59c8-d268-4cc8-af60-4b32b1fd76e6)

It think that we can conclude that it works ;)


If you like my work and don't want me to starve don't hesitate to check my [ko-fi page](https://ko-fi.com/extraltodeus)
