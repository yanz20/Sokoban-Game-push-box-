from pygame.locals import *
import pygame
import sys

class Player:
    x = 40
    y = 40
    box1x = 120
    box1y = 80
    box2x = 80
    box2y = 120
    speed = 40

    def moveRight(self):
        if self.x + self.speed == self.box1x and self.y == self.box1y:
            self.x += self.speed
            self.box1x += self.speed
        elif self.x + self.speed == self.box2x and self.y == self.box2y:
            self.x += self.speed
            self.box2x += self.speed
        else:
            self.x += self.speed
            
    def moveLeft(self):
        if self.x - self.speed == self.box1x and self.y == self.box1y:
            self.x -= self.speed
            self.box1x -= self.speed
        elif self.x - self.speed == self.box2x and self.y == self.box2y:
            self.x -= self.speed
            self.box2x -= self.speed
        else:
            self.x -= self.speed

    def moveUp(self):
        if self.y - self.speed == self.box1y and self.x == self.box1x:
            self.y -= self.speed
            self.box1y -= self.speed
        elif self.y - self.speed == self.box2y and self.x == self.box2x:
            self.y -= self.speed
            self.box2y -= self.speed
        else:
            self.y -= self.speed

    def moveDown(self):
        if self.y + self.speed == self.box1y and self.x == self.box1x:
            self.y += self.speed
            self.box1y += self.speed
        elif self.y + self.speed == self.box2y and self.x == self.box2x:
            self.y += self.speed
            self.box2y += self.speed
        else:
            self.y += self.speed


class Maze:
    def __init__(self):
        self.M = 7
        self.N = 5
        self.maze = [1,1,1,1,1,0,0,
                     1,0,0,0,1,0,0,
                     1,0,1,0,1,1,1,
                     1,0,0,0,0,0,1,
                     1,1,1,1,1,1,1]
    def draw(self, display_surf, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M*self.N):
            if self.maze[ bx + (by*self.M) ] == 1:
                display_surf.blit(image_surf, (bx * 40, by * 40))
            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1

class App:
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._box_surf = None
        self._star_surf = None
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((500,500), pygame.HWSURFACE)
        pygame.display.set_caption('SOKOBAN')
        self._running = True
        self._image_surf = pygame.transform.scale(pygame.image.load("char.png").convert(), (40,40))
        self._block_surf = pygame.transform.scale(pygame.image.load("wall.png").convert(), (40,40))
        self._box_surf = pygame.transform.scale(pygame.image.load("box.png").convert(), (40,40))
        self._star_surf = pygame.transform.scale(pygame.image.load("star.png").convert(), (40,40))

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass
        
    def on_render(self):
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(self._star_surf, (160,120))
        self._display_surf.blit(self._star_surf, (200,120))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        self._display_surf.blit(self._box_surf, (self.player.box1x, self.player.box1y))
        self._display_surf.blit(self._box_surf, (self.player.box2x, self.player.box2y))
        self.maze.draw(self._display_surf, self._block_surf)
        self.validate_win((self.player.box1x, self.player.box1y), (self.player.box2x, self.player.box2y), (160,120),  (200,120))
        pygame.display.flip()

    def validate_win(self, box1, box2, star1, star2):
        star_status = [False, False]
        if box1 == star1:
            star_status[0] = True
        if box1 == star2:
            star_status[1] = True
        if box2 == star1:
            star_status[0] = True
        if box2 == star2:
            star_status[1] = True
        
        if star_status[0] and star_status[1]:
            self._running = False
            print("********\nWin\n********")

    def on_cleanup(self):
        pygame.quit()

    def on_excute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            #pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]) and self._display_surf.get_at(((self.player.x + self.player.speed),self.player.y)) != (251,229,209):
                if self._display_surf.get_at(((self.player.x + self.player.speed),self.player.y)) == (110,68,27) \
                and (self._display_surf.get_at(((self.player.x + 2 * self.player.speed),self.player.y)) == (110,68,27)\
                or self._display_surf.get_at(((self.player.x + 2 * self.player.speed),self.player.y)) == (251,229,209)):
                        pass
                else:
                    self.player.moveRight()

            if (keys[K_LEFT]) and self._display_surf.get_at(((self.player.x - self.player.speed),self.player.y)) != (251,229,209):
                if self._display_surf.get_at(((self.player.x - self.player.speed),self.player.y)) == (110,68,27) \
                and (self._display_surf.get_at(((self.player.x - 2 * self.player.speed),self.player.y)) == (110,68,27)\
                or self._display_surf.get_at(((self.player.x - 2 * self.player.speed),self.player.y)) == (251,229,209)):
                        pass
                else:
                    self.player.moveLeft()

            if (keys[K_UP])  and self._display_surf.get_at((self.player.x, (self.player.y - self.player.speed))) != (251,229,209):
                if self._display_surf.get_at((self.player.x,(self.player.y - self.player.speed))) == (110,68,27) \
                and (self._display_surf.get_at((self.player.x,(self.player.y - 2 * self.player.speed))) == (110,68,27)\
                or self._display_surf.get_at((self.player.x,(self.player.y - 2 * self.player.speed))) == (251,229,209)):
                        pass
                else:
                    self.player.moveUp()

            if (keys[K_DOWN]) and self._display_surf.get_at((self.player.x, (self.player.y + self.player.speed))) != (251,229,209):
                if self._display_surf.get_at((self.player.x,(self.player.y + self.player.speed))) == (110,68,27) \
                and (self._display_surf.get_at((self.player.x,(self.player.y + 2 * self.player.speed))) == (110,68,27)\
                or self._display_surf.get_at((self.player.x,(self.player.y + 2 * self.player.speed))) == (251,229,209)):
                        pass
                else:
                     self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
            pygame.time.wait(100)
        self.on_cleanup()

if __name__ == "__main__":
        theApp = App()
        theApp.on_excute()
        sys.exit()
