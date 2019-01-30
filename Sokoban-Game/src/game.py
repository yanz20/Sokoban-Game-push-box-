"""
This is the main entry point of the game.
"""
import sys
import pygame as pg     # sets pg as an alias for pygame

from core.main import main
from core.main import util
if __name__ == '__main__':
    main()      # Calls the main game loop  - see main.py
    pg.quit()   # Uninitializes all pygame modules
    sys.exit()  # Exits the app

 
