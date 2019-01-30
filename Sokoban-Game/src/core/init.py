"""
Creates and renders the screen.
*** This code is executed by just importing this file
"""
import pygame as pg

from . import constants

pg.init()

_screen = pg.display.set_mode(constants.SCREEN_SIZE)
pg.display.set_caption("SOKOBAN")
pg.draw.rect(_screen, (255,0,0), constants.SCREEN_RECT) #This will draws a rectangle
pg.display.update()
