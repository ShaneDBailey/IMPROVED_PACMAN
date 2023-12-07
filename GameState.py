import pygame
import Constants

class GameState:
    def __init__(self, board):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((Constants.BOARD_WIDTH, Constants.BOARD_HEIGHT))

        self.board = board
        self.state = "play"
        self.clock = pygame.time.Clock()
        self.state_info = {
            "score": 0,
            "lives": 3
        }
        self.key_codes = {
            "w":pygame.K_w,
            "a":pygame.K_a,
            "s":pygame.K_s,
            "d":pygame.K_d
        }
        self.rounds = 0
        self.mood_timer = 0
        self.mood_charts = (
            ("scatter", 7),
            ("chase", 20),
            ("scatter", 7),
            ("chase", 20),
            ("scatter", 5),
            ("chase", 20),
            ("scatter", 5),
            ("chase", 20)
            
        )


    def update(self):
        delta = self.clock.tick(60) / 1000 #time since last frame in miliseconds
        self.screen.fill("black")
        if self.state == "play":
            keys = pygame.key.get_pressed()

            wasd = "".join( [char for char in "wasd" if keys[self.key_codes[char]]] )
            # "" if no keys were pressed. "w" if w was pressed. "wa" if w and a are pressed
            # if "w" in wasd: w was pressed

            if self.rounds < len(self.mood_charts):
                if self.mood_timer == 0:
                    for ghost in self.board.ghosts.values():
                        ghost.mood = self.mood_charts[self.rounds][0]

                self.mood_timer += delta

                if self.mood_timer > self.mood_charts[self.rounds][1]:
                    self.rounds += 1
                    self.mood_timer = 0

            #Update everythingadd
            self.board.update(delta) #This also handles updating the dots
            for ghost in self.board.ghosts.values():
                if ghost is None:
                    continue
                ghost.update(delta, self.board)
                
            self.board.player.update(delta, self.board, wasd)

            #Draw Everything
            self.board.draw(self.screen) #This also handles drawing the dots
            for ghost in self.board.ghosts.values():
                if ghost is None:
                    continue
                ghost.draw(self.screen)
            self.board.player.draw(self.screen)

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        
        pygame.display.flip()

        return True
