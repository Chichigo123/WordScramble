import tkinter as tk
from tkinter import messagebox
import game_utils.Utils as utils
import numpy

class BaseTextBoxManager():

    def clearTextBox(self, event):
        event.widget.delete(0, tk.END)
        event.widget.configure(fg = '#000000')

    def createBasicTextBoxes(self, config, parentFrames, state):
        textBoxesParam = list(zip(config.get("width"), config.get("font"), config.get("relx"), config.get("rely"),
                               config.get("fg"), config.get("bg"), config.get("text"), config.get("relief")))
        textBoxes = []
        if len(textBoxesParam) > 0:
            for textBoxParam in textBoxesParam:
                correctFrameText, correctText, correctFunctionName = utils.getCorrectFrame(parentFrames, textBoxParam[6],
                                                                                           state)
                correctText = tk.StringVar(None)
                correctFrame = getattr(parentFrames, correctFrameText, None)
                entry = tk.Entry(correctFrame, textvariable=correctText, width = textBoxParam[0],
                                 font=textBoxParam[1], fg=textBoxParam[4], bg=textBoxParam[5], relief=textBoxParam[7])
                entry.insert(0, "Type Here")
                entry.place(relx=textBoxParam[2], rely=textBoxParam[3])
                entry.bind("<Button-1>", self.clearTextBox)
                textBoxes.append([entry, correctFunctionName])


        return textBoxes

    def __init__(self):

        pass

class DerivedTextBoxManager(BaseTextBoxManager):
    def setReceiveGameInput(self,):
        self.gameInput = None

    def receiveAndDeleteGameInput(self, event, wordAnswers):
        textBoxes = numpy.array(self.textBoxes, dtype=object)
        textBox = textBoxes[textBoxes[:, 1] == 'GameStartFrame1TextBox0']
        if textBox.shape[0] > 0 and textBox[0][0].get().upper() in wordAnswers:
            self.gameInput = textBox[0][0].get().upper()
        textBox[0][0].delete(0, tk.END)

    def getText(self, action, textBoxName):
        textBoxes = numpy.array(self.textBoxes, dtype=object)
        if action == 'VerifyNameContent':
            textBox = textBoxes[textBoxes[:, 1] == textBoxName]

            if textBox.shape[0] > 0:
                return textBox[0][0].get()

            return ''

    def createBasicTextBoxes(self, config, parentFrames, state):
        self.textBoxes = super().createBasicTextBoxes(config, parentFrames, state)
        return self.textBoxes


    def __init__(self, config, parentFrames, state):
        self.textBoxes = []
        self.gameInput = None
        if config.textBoxConfig:
            self.createBasicTextBoxes(config.textBoxConfig, parentFrames, state)
