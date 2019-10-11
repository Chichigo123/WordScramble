import random

wordListPerLevel = {
    "easy" : ['OPTTAO', 'EPHARCUS', 'HANYE', 'ROAEGN', 'RANGE']
}

wordAnswers = {
    "OPTTAO" : ['POTATO',
                'POT', 'TOP', 'APT', 'TAP', 'TOO'],
    "EPHARCUS" : ['PURCHASE',
                  'PREACH',
                  'CURSE', 'CHASE', 'SPACE', 'CHEAP', 'PEACH', 'CAUSE', 'PURSE',
                  'CURE', 'PUSH', 'SURE', 'CASE', 'CARE',
                  'PEAR',  'HARE', 'HEAP', 'HEAR', 'PURE',
                  'CAPE', 'REAP', 'RACE', 'SEAR'
                  'ARE', 'PEA', 'CAP', 'CAR', 'PEA',  'PAR', 'RAP', 'EAR'],
    "HANYE": ['HYENA',
              'YEAN', 'YEAH',
              'ANY', 'YEN', 'HAY', 'AYE', 'HEN'],
    "ROAEGN": ['ORANGE',
               'GEAR', 'RAGE', 'GONE',
               'ORE', 'ARE', 'RAN', 'RAG'],
    "RANGE": ['ARE', 'AGE']
}


class BaseWordManager():

    def updateWordsList(self, level):
        wordList = wordListPerLevel.get(level)

        answers = []
        wordToPlay = ''
        while True:
            randomIndex = random.randint(0, len(wordList) - 1)
            # wordToPlay = wordList[randomIndex]
            wordToPlay = wordList[3]
            if wordToPlay not in self.alreadyPlayed:
                answers = wordAnswers.get(wordToPlay)
                answers.sort(key = lambda x: [len(x), x], reverse=True)
                self.alreadyPlayed.append(wordToPlay)
                break

        self.answers = answers
        return answers, wordToPlay

    def __init__(self):
        self.alreadyPlayed = []

class DerivedWordManager(BaseWordManager):
    def checkIfGuessedAll(self):
        self.alreadyGuessed.sort(key=lambda x: x, reverse=True)
        if self.answers == self.alreadyGuessed:
            return True
        return False

    def updateAndCheckIfGuessedAll(self, word):
        if word not in self.alreadyGuessed:
            self.alreadyGuessed.append(word)
            return self.checkIfGuessedAll()
        return False

    def __init__(self, level = 'easy'):
        self.alreadyPlayed = []
        self.alreadyGuessed = []
        self.wordListPerLevel = wordListPerLevel.get(level)

