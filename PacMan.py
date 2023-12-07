import Entity
import pygame
import Board
import Constants

class PacMan(Entity.Entity):
    def __init__(self):
        super().__init__(Constants.PACMAN_START)
        self.desired_direction = (0, 0)
        self.speed = 200

    def update(self, delta, board: Board.Board, wasd):
        if "w" in wasd:
            self.desired_direction = (0, -1)
        elif "a" in wasd:
            self.desired_direction = (-1, 0)
        elif "d" in wasd:
            self.desired_direction = (1, 0)
        elif "s" in wasd:
            self.desired_direction = (0, 1)

        #check if we can change the direciton
        if self.fully_inside_square() and not board.get_tile( (self.grid_position[0]+self.desired_direction[0], self.grid_position[1]+self.desired_direction[1]) )["collision"]:
            self.direction = self.desired_direction
        
        if self.can_move_forwards(board):
            self.update_position(self.direction, self.speed, delta)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "yellow",
            self.center(),
            Constants.TILESIZE // 2
        )
        