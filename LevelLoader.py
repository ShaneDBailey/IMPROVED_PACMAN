from Board import Board
import pygame
import Constants
import glob
import Items
import Ghost
import PacMan

def create_board() -> Board:
    board = Board()
    # print("Level Loader :: Loading Sprites")

    # sprite_files = glob.glob(".\\Sprites\\*.png")
    # for file in sprite_files:
    #     print(file)
    #     board.texture_atlas[file] = pygame.image.load(file).convert_alpha()

    print("Level Loader :: Loading Collision Data")
    with open("level_collision.txt", "r") as f:
        level_collision_data = f.read().splitlines()
    print("Level Loader :: First Pass :: Build Map Coarse")
    for y, row in enumerate(level_collision_data):
        for x, cell in enumerate(row):
            match cell:
                case "#":
                    board.level_data[(x,y)] = {
                        "collision":True,
                        "type":"wall"
                    }
                case ".":
                    board.level_data[(x,y)] = {
                        "collision":False,
                        "type":"floor"
                    }
                    board.dots[(x,y)] = Items.Dots(x,y)
                case "!":
                    board.level_data[(x,y)] = {
                        "collision":False,
                        "type":"floor"
                    }
                    board.dots[(x,y)] = Items.BigDots(x,y)
                case "@":
                    board
                    board.level_data[(x,y)] = {
                        "collision":False,
                        "type":"teleporter"
                    }
                case "-":
                    board.level_data[(x,y)] = {
                        "collision":True,
                        "type":"floor"
                    }
                case "_":
                    board.level_data[(x,y)] = {
                        "collision":False,
                        "type":"floor"
                    }
                case _:
                    raise Exception("Level loader reached unknown symbol :: " + cell)
                
    # print("Level Loader :: Second Pass :: Detailing")
    # for y in range(Constants.BOARD_GRID_SIZEY):
    #     for x in range(Constants.BOARD_GRID_SIZEX):
    #         if level_collision_data[(x,y)]["type"] != "wall":
    #             continue
    #         name = ""
    #         north = (x, y-1)
    #         east = (x+1, y)
    #         south = (x, y+1)
    #         west = (x-1, y)
    #         if north in level_collision_data and level_collision_data[north]["type"] == "floor":
    #             name += "N"
    #         if east in level_collision_data and level_collision_data[east]["type"] == "floor":
    #             name += "E"
    #         if south in level_collision_data and level_collision_data[south]["type"] == "floor":
    #             name += "S"
    #         if west in level_collision_data and level_collision_data[west]["type"] == "floor":
    #             name += "W"
    #         level_collision_data[(x, y)]["graphic"] = "wall" + name + ".png"
            


    board.player = PacMan.PacMan()
    board.ghosts["RED_GHOST"] = Ghost.RedGhost()
    board.ghosts["PINK_GHOST"] = Ghost.PinkGhost()
    board.ghosts["BLUE_GHOST"] = Ghost.BlueGhost()
    board.ghosts["ORANGE_GHOST"] = Ghost.OrangeGhost()
    board.redraw_surface()
    return board