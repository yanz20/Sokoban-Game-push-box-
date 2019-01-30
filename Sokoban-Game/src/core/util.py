"""
This Module contains the App class as well as a collection of any important objects or functions
This class is used to keep taking input from user and send to scenemanager,after scenemanager finish, draw() method draws maze on screen 
"""

import pygame as pg
from . import scene_manager
from . import constants
class App:

    def __init__(self):
##        self.now = 0.0
##        self.done = False
##        self.clock = pg.time.Clock()
##        self.fps = 60.0 # Probably not needed
##        self.keys = pg.key.get_pressed()
##        self.scene_manager = scene_manager.SceneManager()
##        self.screen = pg.display.get_surface()
          self.done = False
          self._running = True
          self._display_surf = constants._display_surf
          self._char_surf = constants._char_surf
          self._block_surf = constants._block_surf
          self._box_surf = constants._box_surf
          self._star_surf = constants._star_surf
          self.scene_manager = scene_manager.SceneManager(constants.maze)
        
    def update(self):
        self.now = pg.time.get_ticks()  # time in milliseconds
    
    def on_init(self):
        pg.init()
##        self._display_surf = pg.display.set_mode((500,500), pg.HWSURFACE)
##        pg.display.set_caption('SOKOBAN')
##        self._running = True
##        self._image_surf = pg.transform.scale(pygame.image.load("char.png").convert(), (40,40))
##        self._block_surf = pg.transform.scale(pg.image.load("wall.png").convert(), (40,40))
##        self._box_surf = pg.transform.scale(pg.image.load("box.png").convert(), (40,40))
##        self._star_surf = pg.transform.scale(pg.image.load("star.png").convert(), (40,40))

        
    def event_loop(self):
        """
        Passes events from Pygame into the SceneManager
        """
        if self.on_init() == False:
            self._running = False
##        for event in pg.event.get():
##            if event.type == pg.QUIT: # The user closes the game 
##                self.done = True
            
##        keys = pg.key.get_pressed()
##        if (keys[K_LEFT]):
##            pass                      # To be filled
##        if (keys[K_RIGHT]):
##            pass
##        if (keys[K_UP]):
##            pass
##        if (keys[K_DOWN]):
##            pass
        self.draw()

    def on_cleanup(self):
        pg.quit()
        
    def draw(self):
        sc = self.scene_manager.currentscene
        char = sc.getchar()
        box1 = sc.getbox(0)
        box2 = sc.getbox(1)
        maze = sc.getmaze()
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(self._star_surf, (sc.star1x, sc.star1y))
        self._display_surf.blit(self._star_surf, (sc.star2x, sc.star2y))
        self._display_surf.blit(self._char_surf, (char.getX('UP', 0), char.getY('UP', 0)))
        self._display_surf.blit(self._box_surf, (box1.getX(), box1.getY()))
        self._display_surf.blit(self._box_surf, (box2.getX(), box2.getY()))
        maze.draw(self._display_surf, self._block_surf)
        pg.display.flip()

    def run(self):
        """ 
        Main loop of the game. 
        """

        while not self.done:

            self.event_loop()

            self.update()


