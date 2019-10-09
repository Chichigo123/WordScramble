class BasePlayer():

    def __init__(self, name):
        self.name = name
        self.score = 0


class DerivedPlayer(BasePlayer):


    def __init__(self, name):

        super().__init__(name)