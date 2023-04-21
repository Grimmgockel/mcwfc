import amulet
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist

# load the level
# this will automatically find the wrapper that can open the world and set everything up for you.
RELATIVE_WORLD_PATH = "../../.minecraft/saves/test_world/"
level = amulet.load_format(RELATIVE_WORLD_PATH)

# read a chunk
try:
    chunk = level.get_chunk(0, 0, "minecraft:overworld")
except ChunkDoesNotExist:
    # if a chunk is accessed that does not exist this code will be run.
    print("Chunk does not exist")
except ChunkLoadError:
    # if a chunk is corrupt, is in an unsupported format or
    # just did not load for some reason this code will run.
    # This error would also catch ChunkDoesNotExist if the previous except block did not exist.
    print("Chunk load error")
else:
    # if no errors occurred.
    print(chunk)
    # Chunk(
    #   0,
    #   0,
    #   UnboundedPartial3DArray(dtype=<class 'numpy.uint32'>, shape=(16, inf, 16)),
    #   EntityList([]),
    #   BlockEntityDict()
    # )

    # make changes to the chunk here

# save the changes to the world
level.save()

# close the world
level.close()
