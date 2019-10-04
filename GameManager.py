from WindowManager import *
from ConfigManager import *
from FrameManager import *
from ButtonManager import *

class BaseGameManager():

    def __init__ (self, state):
       self.state = state

    def update_clock(self):
        pass

class DerivedGameManager(BaseGameManager):

    def __init__(self):
        super().__init__('Welcome')

        self.prepareConfiguration()

        self.currentWindow.window.mainloop()


    def updateConfiguration(self):
        self.currentConfig.createFrameConfig(self.state)
        self.currentFrames.destroyFrames()
        self.currentFrames.createBasicFrames(self.currentConfig.frameConfig, self.currentWindow.window)
        self.currentFrames.saveFrameNames(self.currentFrames.runningFrames, self.state)

    def update_clock(self):

        # Checks if a button action is called and requests the game manager to update frames
        if self.state == self.currentFrames.currentButtons.action:
            self.currentWindow.window.after(3000, self.update_clock)
        else:
            self.state = self.currentFrames.currentButtons.action
            self.updateConfiguration()




    def prepareConfiguration(self):

        # Get Window Configuration based on current state
        # Create the Window
        self.currentConfig = DerivedConfigManager(self.state)
        self.currentWindow = DerivedWindowManager(self.currentConfig)

        # Get Frame Configuration based on current state
        # Create the Frames
        self.currentFrames = DerivedFrameManager(self.currentConfig, self.currentWindow.window, self.state)

        # Get Button Configuration based on current state
        # Create the Buttons
        self.currentFrames.currentButtons = DerivedButtonManager(self.currentConfig,  self.currentFrames.frames, self.state)

        self.update_clock()


