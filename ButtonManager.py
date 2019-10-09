import tkinter as tk
from tkinter import messagebox
# from utils.Utils import *
import game_utils.Utils as utils

class ButtonManager():

    def __init__(self):
        self.action = 'Welcome'

    def createBasicButtons(self, config, parentFrames, state):
        buttonsParam = list(zip(config.get("height"), config.get("width"),
                                config.get("relx"), config.get("rely"),
                                config.get("bd"), config.get("bg"),
                                config.get("fg"), config.get("font"),
                                config.get("relief"), config.get("text"),
                                config.get("cursor")))
        buttons = []

        if len(buttonsParam) > 0:
            for buttonParam in buttonsParam:
                correctFrameText, correctText, correctFunctionName = utils.getCorrectFrame(parentFrames, buttonParam[9], state)
                correctFrame = getattr(parentFrames, correctFrameText, None)
                button = tk.Button(correctFrame, bd = buttonParam[4], bg = buttonParam[5],
                                   fg = buttonParam[6], font = buttonParam[7],
                                   relief = buttonParam[8], text = correctText,
                                   cursor = buttonParam[10])
                                 #  command=lambda: self.buttonCallAction(text))
                button.place(relheight=buttonParam[0],
                             relwidth=buttonParam[1],
                             relx=buttonParam[2],
                             rely=buttonParam[3])
                buttons.append([button, correctFunctionName])

        return buttons


class DerivedButtonManager(ButtonManager):

    def callAction_WelcomeFrame0Button0(self):
        messagebox.showinfo("WordScramble Instructions", "Unscramble the letters and find the longest word!")


    def callAction_WelcomeFrame1Button1(self):
        messagebox.showinfo("WordScramble Start", "Welcome to Word Scramble!")
        self.action = 'Choose'

    def callAction_ChooseFrame0Button0(self):
        print('PlaterDetails')
        self.action = 'PlayerDetails'

    def configureButtonCallActions(self, ):

        for idx, (button, frameText) in enumerate(self.buttons):

            if frameText is not None:
                # button['command'] = functionDict[idx]
                button.configure(command = getattr(self, 'callAction_' + frameText, None))

    def __init__(self, config, parentFrames, state):
        if state == 'Welcome' :
            # Start and Instruction Buttons
            super().__init__()
            self.buttons = super().createBasicButtons(config.buttonConfig, parentFrames, state)
            self.configureButtonCallActions()
