import amulet
from amulet.api.block import Block

# load the level
ANVIL_WORLD = "../../AppData/Roaming/.minecraft/saves/test_anvil/"
level = amulet.load_level(ANVIL_WORLD)

# pick a game version that we want to work with
game_version = ("java", (1, 17, 0))

# get a block 
block, block_entity = level.get_version_block(
    0,
    70,
    0,
    "minecraft:overworld",
    game_version,
)

if isinstance(block, Block):
        # Check that what we have is actually a block
        print(block)

# set a block
# define a block in the format of the version we want to work with
block = Block("minecraft", "stone")
level.set_version_block(
    0,
    70,
    0,
    "minecraft:overworld",
    game_version,
    block,
)

# save the changes to the world
level.save()

# close the world
level.close()
