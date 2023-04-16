import amulet

if __name__ == '__main__':
    # load the level
    # level = amulet.level.load_level(r"C:\Users\justi\AppData\Roaming\.minecraft\saves\test\level.dat")
    # level = amulet.load_level("C:\\Users\\justi\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\zjc8ZOe7AAA=\\level.dat")
    # level = amulet.load_level("zjc8ZOe7AAA=")

    # save the changes to the world
    level.save()

    # close the world
    level.close()
