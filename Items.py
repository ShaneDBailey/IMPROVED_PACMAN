#Items.py



import pygame
import Constants


class Items:
    def __init__(self,gridx,gridy):
        self.gridx = gridx
        self.gridy = gridy
        self.frame_count = 0
        self.frame_max = 90
        self.value = None

class Dots(Items):
    def __init__(self,gridx,gridy):
        self.value = 20
        super().__init__(gridx, gridy)

    def draw(self, screen):
        # circle(surface, color, center, radius)
        pygame.draw.circle(
            screen,
            Constants.DOT_COLOR,
            (
                (self.gridx*Constants.TILESIZE)+Constants.TILESIZE/2,
                (self.gridy*Constants.TILESIZE)+Constants.TILESIZE/2,
            ),
            Constants.TILESIZE/6
        )


class BigDots(Items):
    def __init__(self,gridx,gridy):
        self.value = 50
        super().__init__(gridx,gridy)
        self.color_index = 0
        self.color_timer = 0

    def update(self, delta):
        self.color_timer += delta
        if self.color_timer > 0 and self.color_timer < 0.33:
            self.color_index = 0
        elif self.color_timer >= 0.33 and self.color_timer < 0.66:
            self.color_index = 1
        else:
            self.color_timer = 0
            self.color_index = 0

    def draw(self, screen):
        # circle(surface, color, center, radius)
        pygame.draw.circle(
            screen,
            Constants.BIGDOT_COLOR[self.color_index],
            (
                (self.gridx*Constants.TILESIZE)+Constants.TILESIZE/2,
                (self.gridy*Constants.TILESIZE)+Constants.TILESIZE/2,
            ),
            Constants.TILESIZE/3
        )



class Fruits(Items):
    def __init__(self,gridx,gridy,whichFruit):
        self.color = Constants.FRUIT_INDEX[whichFruit].value(0)
        self.value = Constants.FRUIT_INDEX[whichFruit].value(1)

        super().__init__(gridx, gridy)
        
    def draw(self,screen):
        pygame.draw.rect(
            screen, 
            self.color, 
            pygame.Rect
            (
                (self.gridx*Constants.TILESIZE)+Constants.TILESIZE/2,
                (self.gridy*Constants.TILESIZE)+Constants.TILESIZE/2
            ),
            Constants.TILESIZE/2,
            Constants.TILESIZE/2
        )
