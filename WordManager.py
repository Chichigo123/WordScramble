import random

wordListPerLevel = {
    "easy" : ['OPTTAO', 'EPHARCUS', 'HANYE', 'ROAEGN']
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
               'GEAR' 'RAGE', 'GONE'
               'ORE', 'ARE', 'RAN', 'RAG']
}


class BaseWordManager():

    def updateWordsList(self, level):
        wordList = wordListPerLevel.get(level)

        answers = []
        wordToPlay = ''
        while True:
            randomIndex = random.randint(0, len(wordList) - 1)
            # wordToPlay = wordList[randomIndex]
            wordToPlay = wordList[1]
            if wordToPlay not in self.alreadyPlayed:
                answers = wordAnswers.get(wordToPlay)
                answers.sort(key = lambda x: [len(x), x], reverse=True)
                self.alreadyPlayed.append(wordToPlay)
                break

        return answers, wordToPlay

    def __init__(self):
        self.alreadyPlayed = []

class DerivedWordManager(BaseWordManager):

    def __init__(self, level = 'easy'):
        self.alreadyPlayed = []
        self.wordListPerLevel = wordListPerLevel.get(level)

