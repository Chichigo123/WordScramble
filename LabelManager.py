import tkinter as tk
import game_utils.Utils as utils
class BaseLabelManager():

    def __init__(self):

        pass

    def createBasicLabels(self, config, parentFrames, state, ):
        labelsParam = list(zip(config.get("font"), config.get("bg"), config.get("relx"), config.get("rely"),
                               config.get("text"), config.get("fg")))
        labels = []
        if len(labelsParam) > 0:
            for labelParam in labelsParam:
                correctFrameText, correctText, correctFunctionName = utils.getCorrectFrame(parentFrames, labelParam[4], state)
                correctFrame = getattr(parentFrames, correctFrameText, None)
                label = tk.Label(correctFrame, text = correctText, font = labelParam[0], bg = labelParam[1], fg = labelParam[5])
                label.place(relx=labelParam[2], rely=labelParam[3])
                labels.append([label, correctFunctionName])

        return labels

class DerivedLabelManager(BaseLabelManager):
    def updateGameLabel(self, gameInput):
        for label, functionName in self.labels:
            if label.cget("text") == gameInput:
                label.configure(fg = 'black')

    def createBasicLabels(self, config, parentFrames, state, playerLabel = False):
        if not playerLabel:
            self.labels = super().createBasicLabels(config, parentFrames, state)
            return  self.labels
        else:
            self.playerLabels = super().createBasicLabels(config, parentFrames, state)
            return self.playerLabels

    def __init__(self, config, parentFrames, state):
        self.labels = []

        if config.labelConfig:
            self.createBasicLabels(config.labelConfig, parentFrames, state)




