from world import World
from world import Realm

# TODO complex get and set block examples
# TODO chunk access
# TODO handle different spawns, use chat client for chat commands
if __name__ == '__main__':
    MC_PATH = "../../../.minecraft/saves/"
    world = World(MC_PATH + "test_anvil", "java 1.17.0")

    block, block_entity = world.get_block((-200, 4, 86), Realm.OVERWORLD)

    print(block)
    print(block_entity)

    world.save_and_close()



