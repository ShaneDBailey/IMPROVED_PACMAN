import pygame
import Constants
import Board

class Entity(): #Abstract
    def __init__(self, grid_position):
        self.grid_position = grid_position
        self.position = [grid_position[0] * Constants.TILESIZE, grid_position[1] * Constants.TILESIZE]
        self.rect = pygame.Rect( (grid_position[0]*Constants.TILESIZE, grid_position[1]*Constants.TILESIZE), (Constants.TILESIZE, Constants.TILESIZE) )
        self.direction = [0, 0]

    def update_position(self, movement_vector: list[int, int], speed, delta):
        self.position[0] += movement_vector[0] * (speed*delta)
        self.position[1] += movement_vector[1] * (speed*delta)
        self.grid_position = (
            self.position[0] // Constants.TILESIZE,
            self.position[1] // Constants.TILESIZE
        )
        self.rect.topleft = self.position

    def get_current_tile_coords(self):
        return (
            self.grid_position[0]*Constants.TILESIZE, 
            self.grid_position[1]*Constants.TILESIZE
        )

    def center(self) -> list[int, int]:
        return (self.position[0]+(Constants.TILESIZE // 2), self.position[1]+(Constants.TILESIZE // 2))

    def fully_inside_square(self) -> bool:
        t_coords = self.get_current_tile_coords()
        return (
            self.rect.left > t_coords[0] - 3 and
            self.rect.right < t_coords[0] + Constants.TILESIZE + 3 and
            self.rect.top > t_coords[1] - 3 and
            self.rect.bottom < t_coords[1] + Constants.TILESIZE + 3
        )

    def at_intersection(self, board: Board.Board) -> bool:
        if self.fully_inside_square():
            
            #print("I'm fully inside a square")
            print(board.get_neighbors(self.grid_position))
            if len(board.get_neighbors(self.grid_position)) > 2:
                #print("I have more than two neighbors therefore I'm at an intersection")
                return True
        return False
    
    def next_position(self):
        return (self.grid_position[0] + self.direction[0], self.grid_position[1] + self.direction[1])
    
    def can_move_forwards(self, board) -> bool:
        print("Can move forwards?")
        if self.fully_inside_square():
            print("I'm fully inside a square")
            if board.get_tile(self.next_position())["collision"]:
                print("The tile in front of me has collision. I can't move forwards")
                return False
        print("I can move forwards")
        return True

    def get_direction_to(self, target):
        return (target[0]-self.grid_position[0], target[1]-self.grid_position[1])