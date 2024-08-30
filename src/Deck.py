from Card import Card, Suit, Value
import random

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Value]
        random.shuffle(self.cards)

    def shuffle(self):
        n = len(self.cards)
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self):
        return self.cards.pop()

    def reset(self):
        self.__init__()

    def remove(self, card):
        self.cards.remove(card)

    def remove_cards(deck, cards_to_remove):
        for card in cards_to_remove:
            deck.remove(card)
    