import Card

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []  
        self.fold = False
        self.current_bet = 0
        self.isRaise = False


    def setCards(self, card):
        self.hand.append(card)

    def bet(self, amount):
        actual_bet = min(amount, self.chips)
        self.chips -= actual_bet
        self.current_bet = actual_bet
        return actual_bet

    def reset_hand(self):
        self.hand = []
        self.fold = False
        self.current_bet = 0

    def fold_hand(self):
        self.fold = True

    def check(self):
        return 0 

    def call(self, highest_bet):
        call_amount = highest_bet - self.current_bet
        return self.bet(call_amount)
    
    def raise_bet(self, raise_amount):
        self.isRaise = True
        total_bet = raise_amount
        return self.bet(total_bet)
    
    def all_in(self):
        print("all-in")
        all_in_amount = self.chips
        self.current_bet += all_in_amount
        self.chips = 0
        return all_in_amount

    def is_user(self):
        return False

    def make_decision(self, highest_bet):
        raise NotImplementedError("Subclass must implement make_decision method")