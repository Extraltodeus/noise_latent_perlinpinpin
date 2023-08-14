# noise_latent_perlinpinpin
This allows to create latent spaces filled with perlin-based noise that can actually be used by the samplers.

# installation:
Just drop the .py file in your custom nodes folder or download the repository as zip and put it in the custom nodes folder.

You will also need BlenderNeko noise related nodes to use this and the workflow:

https://github.com/BlenderNeko/ComfyUI_Noise

# known limitation:
Some aspect ratio does not work.

# Use

I've included a workflow with notes in it to give you the basics but this is uncharted territory.

Euler works good with normal noise, dpmpp2m with karras is pretty nice.

It was a pain to be able to finally have a noisy usable fractal!

![image](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/22b5e919-8d05-491b-af0c-7c62a78eb6d7)

Now you can reinject the same noise pattern after an upscale and get more coherent results.

This Perlin Merlin Rabbit has been with SDXL using the perlin based noise.

The workflow has been noisy perlin injection -> SDXL Base (15 steps) -> VAE decode -> lanczos resize -> VAE encode -> same seed noisy perlin injection -> SDXL refiner (5 steps)

The lanczos resize nodes are [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos.py) and [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos_to_res.py)

![00296UI_00001_](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/cd06e1e8-e5bd-461a-8e54-f114a83afdf9)
