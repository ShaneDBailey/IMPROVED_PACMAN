import Constants
import pygame
import Items

class Board():
    def __init__(self):
        self.level_data = {}
        self.ghosts = {}
        self.player = None
        self.dots = {}
        self.texture_atlas = {}
        self.teleporters = {
            ()
        }

    def redraw_surface(self):
        print("Board :: Refreshing Surface")
        self.surf = pygame.Surface((Constants.BOARD_WIDTH, Constants.BOARD_HEIGHT))
        tile = pygame.Surface((Constants.TILESIZE, Constants.TILESIZE))
        for y in range(Constants.BOARD_GRID_SIZEY):
            for x in range(Constants.BOARD_GRID_SIZEX):
                # Sprites not implimented
                # self.surf.blit(self.texture_atlas[self.level_data[(x,y)]["graphic"]], (x*Constants.TILESIZE, y*Constants.TILESIZE))
                if self.level_data[(x,y)]["type"] == "wall":
                    tile.fill("blue")
                elif self.level_data[(x,y)]["type"] == "teleporter":
                    tile.fill("purple")
                else:
                    tile.fill("black")
                self.surf.blit(tile, (x*Constants.TILESIZE, y*Constants.TILESIZE))

    def get_tile(self, position):
        return self.level_data[position]

    def get_neighbors(self, grid_position, only_passable=True):
        neighbors = []
        for direction in ((0,-1), (1,0), (0,1), (-1,0)):
            n_pos = (grid_position[0] + direction[0], grid_position[1] + direction[1])
            if n_pos in self.level_data:
                if only_passable:
                    if not self.level_data[n_pos]["collision"]:
                        neighbors.append(n_pos)
                else:
                    neighbors.append(n_pos)
        return neighbors

    def update(self, delta):
        for dot in self.dots.values():
            if isinstance(dot, Items.BigDots):
                dot.update(delta)

    def draw(self, screen):
        screen.blit(self.surf, (0,0))
        for dot in self.dots.values():
            dot.draw(screen)
