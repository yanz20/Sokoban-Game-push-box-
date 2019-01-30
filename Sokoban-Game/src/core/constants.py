"""
Stores all game and configuration constants here.
"""

import pygame as pg


SCREEN_SIZE = (500, 500)
SCREEN_RECT = pg.Rect((0, 0), (50,50))
TIME_PER_UPDATE = 16.0  #Milliseconds
maze = [[1,1,3,2,2,3,4,3,5,3,7,5,
	1,1,1,1,1,0,0,
        1,0,0,0,1,0,0,
        1,0,1,0,1,1,1,
        1,0,0,0,0,0,1,
        1,1,1,1,1,1,1]]
_display_surf = pg.display.set_mode((500,500), pg.HWSURFACE)

_char_surf = pg.transform.scale(pg.image.load("char.png").convert(), (40,40))
_block_surf = pg.transform.scale(pg.image.load("wall.png").convert(), (40,40))
_box_surf = pg.transform.scale(pg.image.load("box.png").convert(), (40,40))
_star_surf = pg.transform.scale(pg.image.load("star.png").convert(), (40,40))
