import Entity
import math
import Board
import Constants
import pygame

class Ghost(Entity.Entity):

    def __init__(self, ghost):
        self.target = None
        self.speed = 100
        self.mood = "chase"
        self.state = "ghost_house"
        self.color = Constants.GHOST_INDEX[ghost][0]
        self.state_info = {"timer": Constants.GHOST_INDEX[ghost][1]}
        self.scatter_target = Constants.GHOST_INDEX[ghost][2]
        super().__init__(Constants.GHOST_INDEX[ghost][3])

    def change_mood(self, mood):
        self.mood = mood
    
    def find_target(self,board):
        raise NotImplementedError("find_target was not overridden")

    def update(self, delta, board: Board.Board):
        self.find_target(board)
        if self.state == "ghost_house":
            self.state_info["timer"] -= delta
            if self.state_info["timer"] <= 0:
                #updating all the positioning
                self.grid_position = Constants.GHOST_START
                self.position = [self.grid_position[0]*Constants.TILESIZE, self.grid_position[1]*Constants.TILESIZE]
                self.rect.topleft = self.position
                #
                self.state = "intersection"
                self.state_info = {"cameFrom":[-1,-1]}
                
        elif self.state == "intersection":
            distance = math.inf if self.mood != "fright" else -math.inf
            tile = None
            if self.mood == "chase":
                target = self.find_target(board)
            elif self.mood == "scatter":
                target = self.scatter_target
            elif self.mood == "fright":
                target = board.player.grid_position

            neighbors = board.get_neighbors(self.grid_position)

            for neighbor in neighbors:
                if neighbor == self.state_info["cameFrom"]:
                    continue
                d = math.dist(neighbor, target)
                if self.mood == "fright":
                    if d > distance:
                        distance = d
                        tile = neighbor
                else:
                    if d < distance:
                        distance = d
                        tile = neighbor

            print(tile, distance)
            assert tile is not None
            self.direction = self.get_direction_to(tile)

            self.state = "moving"

            self.state_info = {
                "cameFrom": self.grid_position
            }

        elif self.state == "moving":
            if self.at_intersection(board) and self.grid_position != self.state_info["cameFrom"]:
                self.state = "intersection"
                self.state_info = {"cameFrom":(self.grid_position[0]-self.direction[0], self.grid_position[1]-self.direction[1])}
            else:
                if self.can_move_forwards(board):
                    self.update_position(self.direction, self.speed, delta)
                else:
                    print(board.get_neighbors(self.grid_position))
                    for neighbor in board.get_neighbors(self.grid_position):
                        if neighbor != (self.grid_position[0]-self.direction[0], self.grid_position[1]-self.direction[1]):
                            print("Turning towards", neighbor)
                            self.direction = self.get_direction_to(neighbor)
                            break
            

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            self.center(),
            Constants.TILESIZE // 2
        )


class RedGhost(Ghost):
    def __init__(self):
        super().__init__("RED_GHOST")

    def find_target(self, board):
        return board.player.grid_position
    
class PinkGhost(Ghost):
    def __init__(self):
        super().__init__("PINK_GHOST")

    def find_target(self,board):
        four_tiles_ahead_of_player = (
            board.player.grid_position[0]+ (board.player.direction[0]*4), 
            board.player.grid_position[1] + (board.player.direction[1]*4)
        )
        return four_tiles_ahead_of_player
    
class BlueGhost(Ghost):
    def __init__(self):
        super().__init__("BLUE_GHOST")

    def find_target(self, board):
        two_tiles_ahead_of_player = (
            board.player.grid_position[0] + (board.player.direction[0]*2),
            board.player.grid_position[1] + (board.player.direction[1]*2)
        )
        red_position = board.ghosts["RED_GHOST"].grid_position
        vector = (red_position[0] - two_tiles_ahead_of_player[0], red_position[1] - two_tiles_ahead_of_player[1])
        return (vector[0]*2, vector[1]*2)
        
        
class OrangeGhost(Ghost):
    def __init__(self):
        super().__init__("ORANGE_GHOST")

    def find_target(self, board):
        if math.dist(self.grid_position, board.player.grid_position) <= 8:
            #go to scatter point
            return Constants.GHOST_INDEX["ORANGE_GHOST"][2]
        else:
            #go to player
            return board.player.grid_position