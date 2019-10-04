import tkinter as tk

class FrameManager():

    def __init__(self):

        pass


    def destroyFrames(self):
        for frame in self.runningFrames:
            frame.destroy()

    def saveFrameNames(self, frames, state):
        for idx, frame in enumerate(frames):
            setattr(self.frames, state + 'Frame' + str(idx), frame)

    def createBasicFrames(self, config, parentWindow):

        framesParam = list(zip(config.get("height"), config.get("width"),
                               config.get("bg"), config.get("relx"),
                               config.get("rely"), config.get("relief"),
                               config.get("borderwidth")))
        frames = []

        for frameParam in framesParam:
            frame = tk.Frame(master = parentWindow, height = frameParam[0], width = frameParam[1],
                             bg=frameParam[2], relief=frameParam[5], borderwidth=frameParam[6])

            # Put the frames into position
            frame.place(relx = frameParam[3], rely = frameParam[4])
            frames.append(frame)

        return frames



class DerivedFrameManager(FrameManager):

    def __init__(self, config, parentWindow, state):
        self.frames =  type('', (), {})()

        frames = super().createBasicFrames(config.frameConfig, parentWindow)
        self.runningFrames = frames

        self.saveFrameNames(frames, state)

