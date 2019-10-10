import tkinter as tk
import numpy
from tkinter import messagebox

def getCorrectFrame( parentFrames, widgetText, state):
    if state in widgetText:
        stateTextIdx = widgetText.find(state)
        correctText = widgetText[: stateTextIdx]

        frameNumberIdx = widgetText.find('Frame')
        correctFrame = state + 'Frame' + str(widgetText[frameNumberIdx + 5])
        correctFunctionName = state + 'Frame' + widgetText[frameNumberIdx + 5: ]

    return correctFrame, correctText, correctFunctionName


def checkIfWordIsFound(event, wordAnswers, textBoxes):
    textBoxes = numpy.array(textBoxes, dtype=object)
    textBox = textBoxes[textBoxes[:, 1] == 'GameStartFrame1TextBox0']
    if textBox.shape[0] > 0 and textBox[0][0].get().upper() in wordAnswers:
        textBox[0][0].delete(0, tk.END)

def verifyPlayerDetails(text, action):
    if action == 'VerifyNameContent' and text == '':
        messagebox.showinfo("Player Details Missing", "Name is mandatory")
        return False
    else:
        messagebox.showinfo("Player Details Successful", f"Welcome Player {text}")
        return True
