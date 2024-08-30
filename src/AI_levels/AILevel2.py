import sqlite3
from Player import Player
from Card import Value, Suit, Card
from Deck import Deck

class AIPlayerLevel2(Player):
    def __init__(self, name, chips):
        super().__init__(name, chips)
        self.preflop_odds = self.load_preflop_odds()

    def load_preflop_odds(self):
        """ Load preflop odds from the database into a dictionary. """
        preflop_odds = {}
        with sqlite3.connect('poker_odds.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT card1, card2, win_rate FROM Preflop")
            rows = cursor.fetchall()
            for row in rows:
                card1, card2, win_rate = row
                preflop_odds[(card1, card2)] = win_rate
                preflop_odds[(card2, card1)] = win_rate  # Ensure both orders are considered the same
        return preflop_odds

    def evaluate_hand_strength(self):
        """ Evaluate the hand strength based on the initial two cards using preflop odds. """
        if len(self.hand) != 2:
            return 0 

        card1, card2 = self.hand
        card1_str = f"{card1.rank.name} of {card1.suit.name}"
        card2_str = f"{card2.rank.name} of {card2.suit.name}"

        if card1.suit == card2.suit:
            card1_str = f"{card1.rank.name} of CLUBS"
            card2_str = f"{card2.rank.name} of CLUBS"
        else:
            card1_str = f"{card1.rank.name} of CLUBS"
            card2_str = f"{card2.rank.name} of HEARTS"


        # Look up the preflop win rate for this combination
        hand_key = (card1_str, card2_str)
        win_rate = self.preflop_odds.get(hand_key, 0)  # Default to 0 if not found

        if win_rate == 0:
            card1_str = f"{card1.rank.name} of HEARTS"
            card2_str = f"{card2.rank.name} of CLUBS"

            hand_key = (card1_str, card2_str)
            win_rate = self.preflop_odds.get(hand_key, 0)

        print(win_rate)

        return win_rate
                    

    def make_decision_pre(self):
        """ Make decision based on hand strength and call if EV is positive. """
        
        hand_strength = self.evaluate_hand_strength()

        # Decision threshold based on win rate
        call_threshold = 45  # Example threshold, can be adjusted
        raise_threshold = 55

        # if hand_strength >= raise_threshold:
        #     print("Raise")
        #     return "Raise"
        # elif hand_strength >= call_threshold:
        #     print("Call")
        #     return "Call"
        # print("Fold")
        return hand_strength  # AI folds if the hand strength is below the threshold
    
 