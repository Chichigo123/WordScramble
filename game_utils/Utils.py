def getCorrectFrame( parentFrames, buttonText, state):
    if state in buttonText:
        stateTextIdx = buttonText.find(state)
        correctText = buttonText[: stateTextIdx]

        frameNumberIdx = buttonText.find('Frame')
        correctFrame = state + 'Frame' + str(buttonText[frameNumberIdx + 5])

    return correctFrame, correctText

