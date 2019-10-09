import tkinter as tk

# Verify only the 'Name' Textbox
specialStates = {'VerifyPlayerDetails': ['PlayerDetailsFrame0TextBox0']}

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
            'bg': bg or ['#b2e9f0', '#b2e9a0'],
            'relx': relx or [0, 0],
            'rely':  rely or [0, 0.8],
            'relief': relief or [tk.SUNKEN, tk.SUNKEN],
            'borderwidth': borderwidth or [0, 0]
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
            'bg': bg or ['#b2e9f0'],
            'fg': fg or ['#2A0100'],
            'font': font or [["Broadway", 20, "bold"]],
            'relief': relief or [[tk.SUNKEN]],
            'text': text or ['Welcome'],
            'cursor': cursor or ['spider']
        }


    def createLabelConfig(self, font = [], bg = [], relx = [], rely = [], text = [], fg = []):
        self.labelConfig = {
            'font': font or [["Broadway", 20, "bold"]],
            'bg': bg or ["#b2e9f0"],
            'relx': relx or [0],
            'rely': rely or [0],
            'text': text or ['None'],
            'fg': fg or ['#2A0100']
        }

    def createTextBoxConfig(self, width = [], font = [], relx = [], rely = [],  fg = [], bg = [], text = []):
        self.textBoxConfig = {
            'width': width or [50],
            'font': font or [["Broadway", 20, "bold"]],
            'bg': bg or ["#b2e9f0"],
            'relx': relx or [0],
            'rely': rely or [0],
            'fg': fg or ['#2A0100'],
            'text': text or ['None']
        }

    def __init__(self):
        self.createWindowConfig()
        self.createFrameConfig()
        self.createButtonConfig()
        self.createLabelConfig()
        self.createTextBoxConfig()

class DerivedConfigManager(BaseConfigManager):
    """
    This is derived of Config Manager
    """

    def __init__(self, state):
        self.createWindowConfig(state)
        self.createFrameConfig(state)
        self.createButtonConfig(state)
        self.createLabelConfig(state)
        self.createTextBoxConfig(state)


    def createWindowConfig(self, state):

        if state == 'Welcome':
          super().createWindowConfig(className = state, geometry = [900, 900], bg = '#b2e9f0')

    def createFrameConfig(self, state):
        self.frameConfig = {}
        if state == 'Welcome':
            super().createFrameConfig()
        elif state == 'Choose':
            super().createFrameConfig(height = [800], width = [800], bg = ['#b2e9f0'], relx = [0],
                                      rely = [0], relief = [tk.SUNKEN], borderwidth = [1])
        elif state == 'PlayerDetails':
            super().createFrameConfig(height = [800], width = [800], bg = ['#b2e9f0'], relx = [0],
                                      rely = [0], relief = [tk.SUNKEN], borderwidth = [1])

        elif state == 'GameStart':
            super().createFrameConfig()

    def createButtonConfig(self, state):
        self.buttonConfig = {}

        if state == 'Welcome':
          super().createButtonConfig(height = [.55, .25], width = [0.5, 0.5], relx = [0.25, 0.25],
                                     rely = [0.1, 0.60] , bd = [3, 3], bg = ['#E0909F', '#E0909F'],
                                     fg = ['#2A0100', '#2A0100'], font = [["Broadway", 20, "bold"], ["Broadway", 20, "bold"]],
                                     relief = [[tk.SUNKEN], [tk.SUNKEN]], text = ['StartWelcomeFrame1Button1', 'InstructionWelcomeFrame0Button0'],
                                     cursor = ['spider', 'heart'])
        elif state == 'Choose':

            super().createButtonConfig(height=[.25, .15], width=[0.5, 0.5], relx=[0.25, 0.25],
                                       rely=[0.1, 0.65], bd=[3, 3], bg=['#E0909F', '#E0909F'],
                                       fg=['#2A0100', '#2A0100'], font=[["Broadway", 20, "bold"], ["Broadway", 20, "bold"]],
                                       relief=[[tk.SUNKEN], [tk.SUNKEN]],
                                       text=['New Player ChooseFrame0Button0', 'Take me to the GameChooseFrame0Button1'],
                                       cursor=['spider', 'heart'])

        elif state == 'PlayerDetails':
            super().createButtonConfig(height=[.05], width=[0.25], relx=[0.2],
                                       rely=[0.25], bd=[1], bg=['#E0909F'],
                                       fg=['#2A0100'], font=[["Helvetica", 10, "bold"]],
                                       relief=[[tk.SUNKEN]],
                                       text=['Submit PlayerDetailsFrame0Button0'],
                                       cursor=['spider'])


    def createLabelConfig(self, state):
        self.labelConfig = {}

        if state == 'Welcome':
            super().createLabelConfig(font = [["Algerian", 30, "bold"]],
                                      bg = ['#b2e9f0'], relx = [0.2], rely = [.1],
                                      text = ['  WORD SCRAMBLE  \n  GAME PLAY  WelcomeFrame0Label0'],
                                      fg = ['#2A0100'])
        if state == 'PlayerDetails':
            super().createLabelConfig(font = [["Broadway", 10, "bold"], ["Broadway", 10, "bold"], ["Broadway", 10, "bold"]],
                                      bg = ['#b2e9f0', '#b2e9f0', '#b2e9f0'], relx = [.1, .1, .1], rely = [.1, .15, .2],
                                      text = ['Name PlayerDetailsFrame0Label0', 'Age PlayerDetailsFrame0Label1',
                                              'Email PlayerDetailsFrame0Label2'],
                                      fg = ['#2A0100', '#2A0100', '#2A0100'])

    def createTextBoxConfig(self, state):
        self.textBoxConfig = []

        if state == 'PlayerDetails':
            super().createTextBoxConfig(width = [30, 30, 30], font = [["Broadway", 10], ["Broadway", 10], ["Broadway", 10]],
                                        relx = [.2, .2, .2], rely = [.1, .15, .2], fg = ['#2A0110', '#2A0110', '#2A0110'],
                                        bg = ['#b2e9b0', '#b2e9b0', '#b2e9b0'],
                                        text = ['Name PlayerDetailsFrame0TextBox0', 'Age PlayerDetailsFrame0TextBox1',
                                                'emailaddress PlayerDetailsFrame0TextBox2'])