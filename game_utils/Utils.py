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


def checkIfWordIsFound(gameInput, wordAnswers):
    if gameInput in wordAnswers:
        return True
    return False


def verifyPlayerDetails(text, action):
    if action == 'VerifyNameContent' and text == '':
        messagebox.showinfo("Player Details Missing", "Name is mandatory")
        return False
    else:
        messagebox.showinfo("Player Details Successful", f"Welcome Player {text}")
        return True

def prompt(text):
    messagebox.showinfo("All Words Found", f"{text}")