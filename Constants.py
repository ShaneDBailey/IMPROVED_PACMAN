

#Board Constants
BOARD_WIDTH = 630
BOARD_HEIGHT = 660
BOARD_GRID_SIZEX = 21
BOARD_GRID_SIZEY = 22

TILESIZE = BOARD_WIDTH // BOARD_GRID_SIZEX

FRAME_RATE = 60


LEFT_PORTAL_POSITION = (0,10)
RIGHT_PORTAL_POSITION = (20,10)


RED_TARGET = (24,-2)
PINK_TARGET = (0,-2)
BLUE_TARGET = (24,28)
YELLOW_TARGET = (0,28)


DOT_COLOR = (255,153,0)
BIGDOT_COLOR = ((255,153,0),(255,224,179))
# todo orange apple melon galaxian bell key
#color,value
FRUIT_INDEX = {
    "Cherry":((204,0,0),100),
    "Strawberry":((255,77,77),300),
    "Orange":((255,153,0),500),
    "Apple":((204,0,0),700),
    "Melon":((0,153,51),1000),
    "Galaxian":((255,255,0),2000),
    "Bell":((255,255,77),3000),
    "Key":((102,255,255),5000)
}

PACMAN_START = (10,12)
#color,timer, scatter_target, grid_position 
GHOST_START = (10,8)
GHOST_INDEX = {
    "RED_GHOST":((255,0,0),3,(24,-2),(10,8)),
    "PINK_GHOST":((255,153,204),6,(0,-2),(10,10)),
    "BLUE_GHOST":((0,255,255),9,(24,28),(9,10)),
    "ORANGE_GHOST":((255,255,0),12,(0,28),(11,10)),
}