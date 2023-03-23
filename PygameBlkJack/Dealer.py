import random


class Dealer:
    def __init__(self):
        self.total = 0
        self.hand = []
        self.cards = ["c01", "c02", "c03", "c04", "c05", "c06", "c07", "c08", "c09", "c10", "c11", "c12", "c13",
            "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "d11", "d12", "d13",
            "h01", "h02", "h03", "h04", "h05", "h06", "h07", "h08", "h09", "h10", "h11", "h12", "h13",
            "s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11", "s12", "s13"]
        self.VALUES = {
        "c01": 11,
        "c02": 2,
        "c03": 3,
        "c04": 4,
        "c05": 5,
        "c06": 6,
        "c07": 7,
        "c08": 8,
        "c09": 9,
        "c10": 10,
        "c11": 10,  # Jack
        "c12": 10,  # Queen
        "c13": 10,  # King
        "d01": 11,
        "d02": 2,
        "d03": 3,
        "d04": 4,
        "d05": 5,
        "d06": 6,
        "d07": 7,
        "d08": 8,
        "d09": 9,
        "d10": 10,
        "d11": 10,  # Jack
        "d12": 10,  # Queen
        "d13": 10,  # King
        "h01": 11,
        "h02": 2,
        "h03": 3,
        "h04": 4,
        "h05": 5,
        "h06": 6,
        "h07": 7,
        "h08": 8,
        "h09": 9,
        "h10": 10,
        "h11": 10,  # Jack
        "h12": 10,  # Queen
        "h13": 10,  # King
        "s01": 11,
        "s02": 2,
        "s03": 3,
        "s04": 4,
        "s05": 5,
        "s06": 6,
        "s07": 7,
        "s08": 8,
        "s09": 9,
        "s10": 10,
        "s11": 10,  # Jack
        "s12": 10,  # Queen
        "s13": 10,  # King
    }
    def deal_card(self, Player):
        chosen_card = random.choice(self.cards)
        self.cards.remove(chosen_card)
        Player.hand.append(chosen_card)

    
    def reset(self):
        self.cards = ["c01", "c02", "c03", "c04", "c05", "c06", "c07", "c08", "c09", "c10", "c11", "c12", "c13",
            "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "d11", "d12", "d13",
            "h01", "h02", "h03", "h04", "h05", "h06", "h07", "h08", "h09", "h10", "h11", "h12", "h13",
            "s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11", "s12", "s13"]
        self.total = 0
        self.hand = []

    def calculate_total(self, player):
        player.total = 0
        num_aces = 0
        for card in player.hand:
            if card.endswith("01"):
                num_aces += 1
            else:
                player.total += self.VALUES[card]
        for i in range(num_aces):
            if player.total + 11 <= 21:
                player.total += 11
            else:
                player.total += 1

        return player.total


        
        
        
