from Player import Player

class AIPlayerLevel1(Player):
    def __init__(self, name, chips):
        super().__init__(name, chips)

    def make_decision(self, highest_bet):
        # AI always calls the highest bet made by Player 1
        if self.current_bet < highest_bet:
            bet_amount = self.call(highest_bet - self.current_bet)
            return bet_amount
        else:
            return 0  # AI checks if no bet is made
