from WindowManager import *
from ConfigManager import *
from FrameManager import *
from ButtonManager import *
from LabelManager import *
from TextBoxManager import *
from WordManager import *
from Player import *

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

    def endGame(self,):
        self.state = 'GameEnd'
        self.currentWindow.window.after_cancel(self.job)
        self.currentWindow.window.destroy()

    def createNewPlayer(self, name, age, email):
        self.player = DerivedPlayer(name, age, email)

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
            if self.wordManager.checkIfAllWordsArePlayed():
                if self.currentLevel != lastLevel:
                    utils.prompt(f"Congratulations! You have finished {self.currentLevel} level")
                else:
                    utils.prompt(f"Congratulations! You have finished the game.\nYour score is {self.score}")
                    self.endGame()
                    return

                if self.player:
                    self.currentLevel = self.wordManager.getNextLevel(self.player.level)
                    self.player.updatePlayerDetails(level = self.currentLevel)
                else:
                    self.currentLevel = self.wordManager.getNextLevel(self.currentLevel)

            if self.player:
                self.currentConfig.createLabelConfigForPlayer(self.player.name, self.player.age, self.player.email,
                                                              self.player.score, self.player.level)
                self.currentFrames.currentLabels.playerLabels = \
                    self.currentFrames.currentLabels.createBasicLabels(self.currentConfig.playerLabelConfig,
                                                                       self.currentFrames.frames, self.state,
                                                                       playerLabel=True)
            else:
                self.currentConfig.createLabelConfigForPlayer('N/A', 'N/A', 'N/A', self.score, self.currentLevel)
                self.currentFrames.currentLabels.playerLabels = \
                    self.currentFrames.currentLabels.createBasicLabels(self.currentConfig.playerLabelConfig,
                                                                       self.currentFrames.frames, self.state,
                                                                       playerLabel=True)

            self.wordAnswers, self.wordAnswer = self.wordManager.updateWordsList(self.currentLevel)
            self.currentConfig.createWordGameLabelConfig(self.state, self.wordAnswers, self.wordAnswer)
            self.currentWindow.window.bind('<Return>', lambda event:
                self.currentFrames.currentTextBoxes.receiveAndDeleteGameInput(event, self.wordAnswers))
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
                nameInTextBox = self.currentFrames.currentTextBoxes.getText(action = textBoxAction,
                                                                            textBoxName = textBoxNames.get('Name'))
                ageInTextBox = self.currentFrames.currentTextBoxes.getText(action = textBoxAction,
                                                                            textBoxName = textBoxNames.get('Age'))
                emailInTextBox = self.currentFrames.currentTextBoxes.getText(action = textBoxAction,
                                                                            textBoxName = textBoxNames.get('Email'))
                if utils.verifyPlayerDetails(nameInTextBox, textBoxAction):
                    self.currentFrames.currentButtons.setStateOneStepForward(self.currentFrames.currentButtons.nextAction)
                    self.createNewPlayer(nameInTextBox, ageInTextBox, emailInTextBox)
                else:
                    self.currentFrames.currentButtons.setStateOneStepBack(self.currentFrames.currentButtons.previousAction)

        else:
            if self.state == 'GameStart':
                if self.currentFrames.currentTextBoxes.gameInput is not None:
                    gameInput = self.currentFrames.currentTextBoxes.gameInput
                    if utils.checkIfWordIsFound(gameInput, self.wordAnswers):
                        self.currentFrames.currentLabels.updateGameLabel(gameInput)
                        if self.wordManager.updateAndCheckIfGuessedAll(gameInput):
                           utils.prompt('Congratulations! Moving on to next word!')

                           self.score += self.wordManager.getScore()
                           if self.player:
                                self.player.updatePlayerDetails(score=self.score)

                           self.updateConfiguration()
                    self.currentFrames.currentTextBoxes.setReceiveGameInput()

            elif self.state != self.currentFrames.currentButtons.action:
                self.state = self.currentFrames.currentButtons.action
                self.updateConfiguration()

        self.job = self.currentWindow.window.after(1000, self.update_clock)

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

        self.player = None
        self.currentLevel = startingLevel
        self.score = 0
        self.update_clock()


