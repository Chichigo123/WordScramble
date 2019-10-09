class BasePlayer():

    def __init__(self, name, age, emailaddress):
        self.name = name
        self.age = age
        self.emailaddress = emailaddress
        self.score = 0


class DerivedPlayer(BasePlayer):

    def __init__(self, name):

        super().__init__(name, age, emailaddress)