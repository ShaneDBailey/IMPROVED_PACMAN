import LevelLoader
import GameState
#import Board
import pygame

if __name__ == "__main__":
    board = LevelLoader.create_board()
    state = GameState.GameState(board)

    #update returns false if the exit button was pressed
    while state.update():
        pass

    print("Thank you for playing")