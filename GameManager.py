from WindowManager import *
from ConfigManager import *
from FrameManager import *
from ButtonManager import *
from LabelManager import *
from TextBoxManager import *
from WordManager import *

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
        if self.currentConfig.frameConfig:
            self.currentFrames.createBasicFrames(self.currentConfig.frameConfig, self.currentWindow.window, self.state)


        self.currentConfig.createButtonConfig(self.state)
        if self.currentConfig.buttonConfig:
            self.currentFrames.currentButtons.buttons = \
                self.currentFrames.currentButtons.createBasicButtons(self.currentConfig.buttonConfig, self.currentFrames.frames, self.state)
            self.currentFrames.currentButtons.configureButtonCallActions()

        if self.state == 'GameStart':
            wordAnswers, wordAnswer = self.wordManager.updateWordsList('easy')
            self.currentConfig.createWordGameLabelConfig(self.state, wordAnswers, wordAnswer)
            self.currentWindow.window.bind('<Return>', lambda event:
                                            utils.checkIfWordIsFound(event, wordAnswers, self.currentFrames.currentTextBoxes.textBoxes))
        else:
            self.currentConfig.createLabelConfig(self.state)

        if self.currentConfig.labelConfig:
            self.currentFrames.currentLabels.labels = \
                self.currentFrames.currentLabels.createBasicLabels(self.currentConfig.labelConfig, self.currentFrames.frames, self.state)

        self.currentConfig.createTextBoxConfig(self.state)
        if self.currentConfig.textBoxConfig:
            self.currentFrames.currentTextBoxes.textBoxes = \
                self.currentFrames.currentTextBoxes.createBasicTextBoxes(self.currentConfig.textBoxConfig, self.currentFrames.frames,
                                                                         self.state)

    def update_clock(self):

        # Checks if a button action is called and requests the game manager to update frames
        if self.currentFrames.currentButtons.action in specialStates.keys():
            textBoxAction = ''
            for button, frameText in self.currentFrames.currentButtons.buttons:
                if "PlayerDetailsFrame0Button0" == frameText:
                    textBoxAction = "VerifyNameContent"

            if textBoxAction == 'VerifyNameContent':
                textInTextBox = self.currentFrames.currentTextBoxes.getText(action = textBoxAction,
                                                                            textBoxName = specialStates.get(self.currentFrames.currentButtons.action))
                if utils.verifyPlayerDetails(textInTextBox, textBoxAction):
                    self.currentFrames.currentButtons.setStateOneStepForward(self.currentFrames.currentButtons.nextAction)
                else:
                    self.currentFrames.currentButtons.setStateOneStepBack(self.currentFrames.currentButtons.previousAction)

        else:
            if self.state != self.currentFrames.currentButtons.action:
                self.state = self.currentFrames.currentButtons.action
                self.updateConfiguration()

        self.currentWindow.window.after(1000, self.update_clock)

    def prepareConfiguration(self):
        #Create the basic objects

        # Get Window Configuration based on current state
        # Create the Window Object
        self.currentConfig = DerivedConfigManager(self.state)
        self.currentWindow = DerivedWindowManager(self.currentConfig)

        # Get Frame Configuration based on current state
        # Create the Frames Object
        self.currentFrames = DerivedFrameManager(self.currentConfig, self.currentWindow.window, self.state)

        # Get Button Configuration based on current state
        # Create the Buttons Object
        self.currentFrames.currentButtons = DerivedButtonManager(self.currentConfig,  self.currentFrames.frames, self.state)

        # Get Label Configuration based on current state
        # Create the Labels Object
        self.currentFrames.currentLabels = DerivedLabelManager(self.currentConfig, self.currentFrames.frames, self.state)

        # Get Text Box Configuration based on current state
        # Create the TextBox Object
        self.currentFrames.currentTextBoxes = DerivedTextBoxManager(self.currentConfig, self.currentFrames.frames, self.state)

        # Get Word Manager Configuration based on current state
        # Create the WordManager Object
        self.wordManager = DerivedWordManager()

        self.update_clock()


