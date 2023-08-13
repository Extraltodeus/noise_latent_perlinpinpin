# noise_latent_perlinpinpin
This allows to create latent spaces filled with perlin-based noise that can actually be used by the samplers.

# installation:
Just drop the .py file in your custom nodes folder or download the repository as zip and put it in the custom nodes folder.

You will also need BlenderNeko noise related nodes to use this and the workflow:

https://github.com/BlenderNeko/ComfyUI_Noise

# Use

I've included a workflow with notes in it to give you the basics but this is uncharted territory.

Euler works good with normal noise, dpmpp2m with karras is pretty nice.

It was a pain to be able to finally have a noisy usable fractal!

![image](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/22b5e919-8d05-491b-af0c-7c62a78eb6d7)

Now you can reinject the same noise pattern after an upscale and get more coherent results (I haven't actually tried yet but that's the idea that made me do this)

Look at this happy perlin fluffy dog!

![image](https://github.com/Extraltodeus/noise_latent_perlinpinpin/assets/15731540/1b489821-632a-47cd-90c9-df35e876c579)
