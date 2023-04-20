# mcwfc

Here's a basic outline of how you might use these tools together to generate custom biomes:

- First, you'll need to create your custom biome samples. These could be small 16x16 or 32x32 chunks that represent the features of your biome, such as terrain, vegetation, and structures. You can create these using Minecraft or any other tool that allows you to design and export custom chunks.

- Next, you'll need to use the Amulet Core library to create a custom world. This will allow you to generate your biomes and place them in the world. You can use the World.create() method to create a new world, and then use the World.get_chunk() method to get the chunk data for each chunk in the world.

- Once you have your custom biomes and your world set up, you can use the WFC algorithm to generate a larger, seamless biome by tiling together your custom chunks. To do this, you'll need to create a tileset from your custom biome samples, and then use the WFC algorithm to generate a new, larger tileset that is a composite of your smaller chunks.

- Finally, you can use the World.set_chunk() method to place your generated biome chunks in the world. You may need to generate multiple chunks at a time to ensure that they align properly.

'''
wfc/
├── __init__.py
├── generator.py
├── tileset.py
└── wfc_algorithm/
    ├── __init__.py
    ├── constraints.py
    ├── propagator.py
    ├── wave.py
    └── wfc.py

'''

- __init__.py files are empty files that mark a directory as a Python package.
- generator.py contains the main function that uses the Tileset and WFC classes to generate the composite tileset and render the output.
- tileset.py contains the Tileset class that handles loading the custom biome samples and generating the composite tileset using the WFC algorithm.
- wfc_algorithm is a directory that contains the implementation of the WFC algorithm. It's split into multiple files to make it more modular and easier to understand.
- wfc_algorithm/__init__.py is an empty file that marks wfc_algorithm as a Python package.
- wfc_algorithm/constraints.py contains classes for defining constraints that must be satisfied when generating the output.
- wfc_algorithm/propagator.py contains classes for propagating information through the output to ensure constraints are satisfied.
- wfc_algorithm/wave.py contains classes for representing the wave function that encodes the possible output configurations.
- wfc_algorithm/wfc.py contains the WFC class that handles the overall WFC algorithm.