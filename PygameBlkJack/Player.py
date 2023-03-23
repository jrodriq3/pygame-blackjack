class Player:
    def __init__(self):
        self.total = 0
        self.hand = []
        self.stand = False
    def reset(self):
        self.total = 0
        self.hand = []
        self.stand = False