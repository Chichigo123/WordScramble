import tkinter as tk

class BaseConfigManager():

    def createWindowConfig(self, className, geometry, bg):
        self.windowConfig = {
            'screenName': None,
            'baseName':  None,
            'className': className or 'TKWindow',
            'useTk': 1,
            'geometry': [800, 800] or geometry,
            'bg': bg or 'white'
        }

    def createFrameConfig(self, height = [], width = [], bg = [], relx = [], rely = [], relief = [], borderwidth = []):

        # default frame config divided into upper and lower part
        # upper part will contain the words
        # lower part will contain the text box
        self.frameConfig = {
            'height': height or [640, 160],
            'width': width or [800, 800],
            'bg': bg or ['pink', 'gray'],
            'relx': relx or [0, 0],
            'rely':  rely or [0, 0.8],
            'relief': relief or [tk.SUNKEN, tk.SUNKEN],
            'borderwidth': borderwidth or [1, 1]
        }

    def createButtonConfig(self, height = [], width= [], bd = [], bg = [], fg = [],
                           font = [], relief = [], text = [], relx = [], rely = [],
                           cursor = []):

        self.buttonConfig = {
            'height': height or [.25],
            'width': width or [0.25],
            'relx': relx or [0.35],
            'rely': rely or [0.1],
            'bd': bd or [3],
            'bg': bg or ['pink'],
            'fg': fg or ['white'],
            'font': font or [["Broadway", 20, "bold"]],
            'relief': relief or [[tk.SUNKEN]],
            'text': text or ['Welcome'],
            'cursor': cursor or ['spider']
        }

    def __init__(self):
        self.createWindowConfig()
        self.createFrameConfig()
        self.createButtonConfig()

class DerivedConfigManager(BaseConfigManager):
    """
    This is derived of Config Manager
    """

    def __init__(self, state):
        self.createWindowConfig(state)
        self.createFrameConfig(state)
        self.createButtonConfig(state)


    def createWindowConfig(self, state):

        if state == 'Welcome':
          super().createWindowConfig(className = state, geometry = [900, 900], bg = 'black')

    def createFrameConfig(self, state):
        self.frameConfig = {}
        if state == 'Welcome':
            super().createFrameConfig()
        elif state == 'Choose':
            super().createFrameConfig(height = [800], width = [800], bg = ['black'], relx = [0],
                                      rely = [0], relief = [tk.SUNKEN], borderwidth = [1])
        elif state == 'PlayerDetails':
            super().createFrameConfig(height = [800], width = [800], bg = ['white'], relx = [0],
                                      rely = [0], relief = [tk.SUNKEN], borderwidth = [1])

    def createButtonConfig(self, state):
        self.buttonConfig = {}

        if state == 'Welcome':
          super().createButtonConfig(height = [.55, .35], width = [0.5, 0.5], relx = [0.25, 0.25],
                                     rely = [0.1, 0.60] , bd = [3, 3], bg = ['pink', 'gray'],
                                     fg = ['white', 'white'], font = [["Broadway", 20, "bold"], ["Broadway", 20, "bold"]],
                                     relief = [[tk.SUNKEN], [tk.SUNKEN]], text = ['StartWelcomeFrame1Button1', 'InstructionWelcomeFrame0Button0'],
                                     cursor = ['spider', 'heart'])
        elif state == 'Choose':

            super().createButtonConfig(height=[.25, .15], width=[0.5, 0.5], relx=[0.25, 0.25],
                                       rely=[0.1, 0.65], bd=[3, 3], bg=['pink', 'gray'],
                                       fg=['white', 'white'], font=[["Broadway", 20, "bold"], ["Broadway", 20, "bold"]],
                                       relief=[[tk.SUNKEN], [tk.SUNKEN]],
                                       text=['New Player ChooseFrame0Button0', 'Continue GameChooseFrame0Button1'],
                                       cursor=['spider', 'heart'])

