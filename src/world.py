import amulet
from amulet.api.block import Block
import platform
from enum import Enum


class Realm(Enum):
    OVERWORLD = 0
    NETHER = 1
    THE_END = 2

    def __str__(self):
        return "minecraft:" + self.name.lower()


class World:
    def __init__(self, world_name, version):
        # set world name
        self.world_name = world_name

        # construct path to world data
        # TODO absolute paths
        os_name = platform.system()

        system_path = ""
        if os_name == "Windows":
            system_path = "../../AppData/Roaming/"
        elif os_name == "Linux":
            system_path = "../../../"
        world_path = ".minecraft/saves/"
        self.world_path = system_path + world_path + self.world_name + "/"

        # construct version tuple from string "<version_name> <version_number>"
        version_components = version.split(" ")
        version_name = version_components[0]
        version_number = tuple(map(int, version_components[1].split(".")))
        self.version = (version_name, version_number)

        # load level
        self._level = amulet.load_level(self.world_path)

    def save_and_close(self):
        self._level.save()
        self._level.close()

    def set_block(self, coordinates, block_string, realm):
        assert isinstance(coordinates, tuple), "Coordinates has to be a tuple"
        assert len(coordinates) == 3, "Coordinates must have x, y and z"
        block = Block("minecraft", block_string)
        self._level.set_version_block(
            coordinates[0],
            coordinates[1],
            coordinates[2],
            realm.__str__(),
            self.version,
            block,
        )

    def get_block(self, coordinates, realm):
        assert isinstance(coordinates, tuple), "Coordinates has to be a tuple"
        assert len(coordinates) == 3, "Coordinates must have x, y and z"
        block, block_entity = self._level.get_version_block(
            coordinates[0],
            coordinates[1],
            coordinates[2],
            realm.__str__(),
            self.version,
        )
        return block, block_entity
