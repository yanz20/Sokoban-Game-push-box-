
import re
import pygame as pg
class SceneManager:
    """
    SceneManager handles all the specific scenes of the game as well as all scene changes.
    """
    def __init__(self, s):# s is list of mazes(which is list of integer specified in Scene class.)
        self.scenes = s
        self.done = False
        self.restart= False
        self.now = None
        self.current = 0# self.current is used to indicate which level we are currently in
        self.currentscene = None
        self.switch_scene(self.current)
            
    
    def update(self, keys, now):
        """
        Update function that will be called periodically from the main loop.
        Will check if a Scene is done or if the game has ended.
        """
        self.now = now
        if self.currentscene.done:
            self.current += 1
            self.switch_scene(self.current)
        elif self.restart:
            self.switch_scene(self.current)
        self.currentscene.update(keys, now)
    
    def switch_scene(self, i):
        """
        Called when the current scene is complete or user restart, this will initialize the maze for level i.
        """
        self.currentscene = Scene(self.scenes[i])

##        self.scene_name = self.scene.next   #Set the current scene to be played to what the old scene specified as next
##        self.scene.cleanup()
##        self.scene = self.scenes[self.scene_name]   #Retrieve scene from the collection of scenes
##        self.scene.previous = previous
    
    def get_event(self, event):
        """
        Pass event from main game loop to the current scene.Then we modify the char, and box 
        """
        self.currentscene.get_event(event)
    




class Scene:
    """
    All scenes in the game will inherit from this class. Scenes are the different types of views
    throughout the game such as the main menu and every level.
    """
    def __init__(self,s):
        self.speed = 40 # A variable should store speed and saved in constants.py, now just use 40.
        self.char = Character(s[0],s[1],self.speed)
        self.Boxes = []
        self.Boxes.append( Box(s[2],s[3],self.speed))
        self.Boxes.append( Box(s[4],s[5],self.speed))
        self.star1x = s[6]*self.speed
        self.star1y = s[7]*self.speed
        self.star2x = s[8]*self.speed
        self.star2y = s[9]*self.speed
        self.maze = Maze(s[10:])
	self.done= False
    # Here we assume the input format for s is an integer list =[charx,chary,
    #                                                           box1x,box1y,
    #                                                            box2x,box2y,
    #                                                           star1x,star1y,
    #                                                            star2x,star2y
    #
    #                                                            x-dim,y-dim  //Dimensions of the maze
    #                                                           then the maze using 0(wall) and 1(ground)]
    # each level is an integer list, we have a list of integer list to load all the levels in scenemanager.

        # self.persist = {} # TODO ->  Can be used for persisting data such as highscores

    def getchar(self):
        return self.char

    def getbox(self, i):
        if(i==0):
            return self.Boxes[0]
        elif(i==1):
            return self.Boxes[1]

    def getmaze(self):
        return self.maze
"""
Following methods may be used later.
"""    
##    '''
##    def start(self, persistant):
##        """
##        Used to pass persisted data into the Scene
##        """
##        self.persist = persistant
##    '''
##    
##
##    def get_event(self, event):
##        """
##        Processes events passed from the main game loop.
##        All classes that extend this class will overload this function
##        """
##        # We use the pass statement here because python does not allow empty functions and the implementation will be handled by the children of the class
##        pass   
##    
##    def cleanup(self):
##        self.done = False #!!
##    
##    def update(self, keys, now):
##        pass


class Character:
    """
    This initialize the character's position in each level
    """
    def __init__(self,x,y,s):
        self.x = x * s ## this is the coordinate in the screen.
        self.y = y * s
        self.speed = s

    def move(self,key):
        if(key == 'UP'):
            self.y -= self.speed
        elif(key == 'DOWN'):
            self.y += self.speed
        elif(key == 'RIGHT'):
            self.x += self.speed
        elif(key == 'LEFT'):
            self.x -= self.speed

    def getX(self,key,i): ## get methods are used in loop to return the coordiante we gonna check.
        if(key == 'UP'):
            return self.x
        elif(key == 'DOWN'):
            return self.x
        elif(key == 'RIGHT'):
            return self.x + i*self.speed
        elif(key == 'LEFT'):
            return self.x - i*self.speed
        
    def getY(self,key,i):
        if(key == 'UP'):
            return self.y - i*self.speed
        elif(key == 'DOWN'):
            return self.y + i*self.speed
        elif(key == 'RIGHT'):
            return self.y
        elif(key == 'LEFT'):
            return self.y
        
class Box:
    """
    This initialize the box's position in each level
    """
    def __init__(self,x,y,s):
        self.x = x * s
        self.y = y * s
        self.speed = s

    def move(self,key):
        if(key == 'UP'):
            self.y -= self.speed
        elif(key == 'DOWN'):
            self.y += self.speed
        elif(key == 'RIGHT'):
            self.x += self.speed
        elif(key == 'LEFT'):
            self.x -= self.speed

    def getX(self): ## will use the get method to check if the box cover a star
        return self.x
        
    def getY(self):
        return self.y

class Maze:
    def __init__(self,s):
        self.M = s[0]
        self.N = s[1]
        self.maze = s[2:]
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
