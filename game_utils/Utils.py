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

def verifyPlayerDetails(textBoxes, buttons, textBoxNames):
    textBoxes = numpy.array(textBoxes, dtype=object)
    for button, frameText in buttons:
        if frameText == 'PlayerDetailsFrame0Button0':
            for textBoxName in textBoxNames:
                textBox = textBoxes[textBoxes[:, 1] == textBoxName]
                if (textBox.shape[0] > 0 and (textBox[0][0].get() is '')):
                    messagebox.showinfo("Player Details Missing", "Name is mandatory")
                    return False
                else:
                    name = textBox[0][0].get()
                    messagebox.showinfo("Player Details Successful", f"Welcome Player {name}")
                    return True

