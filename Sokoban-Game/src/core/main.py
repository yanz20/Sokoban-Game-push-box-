
from . import util
#from . import init #this creates a window, I currently disable it.
#from .scenes import menu

def main():
    print('This is main function')
    app = util.App()

    # Scene definitions
##    scenes = {
##        "MENU": menu.Menu(),
##    }
    
    #app.scene_manager.setup_scenes(scenes, "MENU")
    app.run()
    
