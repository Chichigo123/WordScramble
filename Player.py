from ConfigManager import defaulTextinTextBox
class BasePlayer():

    def __init__(self, name, age, emailaddress, score = 0, level = 'easy'):
        self.name = name
        if age == defaulTextinTextBox:
            age = ''
        if emailaddress == defaulTextinTextBox:
            emailaddress = ''
        self.age = age
        self.email = emailaddress
        self.score = score
        self.level = level

class DerivedPlayer(BasePlayer):
    def updatePlayerDetails(self, level = None, score = None):
        if level:
            self.level = level
        if score:
            self.score = score

    def __init__(self, name, age, emailaddress):

        super().__init__(name, age, emailaddress)