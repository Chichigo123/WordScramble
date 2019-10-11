import random

wordListPerLevel = {
    "easy" : ['OPTTAO','RANGE'],
    "average": ['HANYE', 'ROAEGN'],
    "difficult": ['EPHARCUS']#, 'RIBAN']
}

wordAnswers = {
    "OPTTAO" : ['POTATO',
                'POT', 'TOP', 'APT', 'TAP', 'TOO'],
    "EPHARCUS" : ['PURCHASE',
                  'PREACH'],
                  # 'CURSE', 'CHASE', 'SPACE', 'CHEAP', 'PEACH', 'CAUSE', 'PURSE',
                  # 'CURE', 'PUSH', 'SURE', 'CASE', 'CARE',
                  # 'PEAR',  'HARE', 'HEAP', 'HEAR', 'PURE',
                  # 'CAPE', 'REAP', 'RACE', 'SEAR'
                  # 'ARE', 'CAP', 'CAR', 'PEA',  'PAR', 'RAP', 'EAR'],
    "RIBAN" : ['BRAIN', 'RAIN'],
    "HANYE": ['HYENA',
              'YEAN', 'YEAH',
              'ANY', 'YEN', 'HAY', 'AYE', 'HEN'],
    "ROAEGN": ['ORANGE',
               'GEAR', 'RAGE', 'GONE', 'NEAR', 'GORE',
               'ORE', 'ARE', 'RAN', 'RAG', 'EAR', 'AGE'],
    "RANGE": ['ARE', 'AGE']
}


class BaseWordManager():

    def getNextLevel(self, level):
        if level == 'easy':
            return 'average'
        elif level == 'average':
            return 'difficult'

    def checkIfAllWordsArePlayed(self):
        if len(self.alreadyPlayed) != 0 and (len(self.alreadyPlayed) == len(self.wordList)):
            self.alreadyPlayed = []
            self.alreadyGuessed = []
            self.answers = []
            return True
        return False

    def updateWordsList(self, level):
        wordList = wordListPerLevel.get(level)

        answers = []
        wordToPlay = ''

        while True:
            randomIndex = random.randint(0, len(wordList) - 1)
            wordToPlay = wordList[randomIndex]
            # wordToPlay = wordList[3]
            if wordToPlay not in self.alreadyPlayed:
                answers = wordAnswers.get(wordToPlay)
                answers.sort(key = lambda x: [len(x), x], reverse=True)
                self.alreadyPlayed.append(wordToPlay)
                break
        self.wordList = wordList
        self.answers = answers
        return answers, wordToPlay

    def __init__(self):
        self.alreadyPlayed = []

class DerivedWordManager(BaseWordManager):

    def getScore(self):
        return self.score

    def checkIfGuessedAll(self):
        self.alreadyGuessed.sort(key=lambda x:  [len(x), x], reverse=True)
        if self.answers == self.alreadyGuessed:
            self.score = len(self.answers)
            self.answers = []
            self.alreadyGuessed = []
            return True
        return False

    def updateAndCheckIfGuessedAll(self, word):
        if word not in self.alreadyGuessed:
            self.alreadyGuessed.append(word)
            return self.checkIfGuessedAll()
        return False

    def __init__(self, level = 'easy'):
        self.wordList = []
        self.alreadyPlayed = []
        self.alreadyGuessed = []
        self.wordListPerLevel = wordListPerLevel.get(level)
        self.score = 0

