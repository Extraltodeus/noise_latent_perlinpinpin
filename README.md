# noise_latent_perlinpinpin
This allows to create latent spaces filled with perlin-based noise that can actually be used by the samplers.

# installation:
Just drop the .py file in your custom nodes folder or download the repository as zip and put it in the custom nodes folder.

You will also need BlenderNeko noise related nodes to use this and the workflow:

https://github.com/BlenderNeko/ComfyUI_Noise

# known limitation:
- Only multiples of 64 can be used for the resolutions or it will throw an error.
- If a kitten sneezes on the wrong setting from a distance it might just break everything.

# Use

I've included a workflow with notes in it to give you the basics but this is uncharted territory.

Euler works good with normal noise, dpmpp2m with karras is pretty nice.

It was a pain to be able to finally have a noisy usable fractal!

![image](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/22b5e919-8d05-491b-af0c-7c62a78eb6d7)

Now you can reinject the same noise pattern after an upscale and get more coherent results.

# What's the idea?

The idea is to generate multiple batches (that's the "noise_iteration" parameter) of perlin noise, then multiply them together to "break" the usual perlin pattern and scatter the noise. Then substracting the mean value so to "center" the value distribution and make it look like the usual noise distribution while keeping the fractal property.

The "persistence" setting being basically a multiplication factor for each layer has a strong effect.

"reduce_near_zero_factor" will start to "compress" the values towards zero to make the value distribution more "gaussian".

Finding the right settings for this was really like aiming at the moon with a slingshot. I guess that if I had made more evolved noise analysis tools rather than printing the value distribution in the terminal it would have made things a little easier.

# Example / Idea

This Perlin Merlin Rabbit has been made with SDXL using the perlin based noise.

The workflow has been noisy perlin injection -> SDXL Base (15 steps) -> VAE decode -> lanczos resize (x1.5) -> VAE encode -> same seed noisy perlin injection (but 1.5x bigger) -> SDXL refiner (5 steps)

The lanczos resize nodes are [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos.py) and [here](https://github.com/Extraltodeus/CustomComfyUINodes/blob/main/image_lanczos_to_res.py)

![00296UI_00001_](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/cd06e1e8-e5bd-461a-8e54-f114a83afdf9)
