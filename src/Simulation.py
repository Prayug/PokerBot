from multiprocessing import Pool, cpu_count
import os
import sqlite3
import sys

from Player import Player
from Card import Card, Suit, Value
from Game import PokerGame 

def create_hands_table():
    with sqlite3.connect('poker_odds_newShuffle.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Preflop (
                card1 TEXT,
                card2 TEXT,
                win_rate REAL,
                high_card REAL,
                one_pair REAL,
                two_pair REAL,
                three_of_a_kind REAL,
                straight REAL,
                flush REAL,
                full_house REAL,
                four_of_a_kind REAL,
                straight_flush REAL,
                royal_flush REAL
            )
        ''')
        conn.commit()

def num_of_calculations():
    unique_combinations = set()
    hand = tuple(sorted([("TWO", "CLUBS"), ("TWO", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("THREE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("FOUR", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("FIVE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("SIX", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("TWO", "CLUBS"), ("THREE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("FOUR", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("FIVE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("SIX", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("SEVEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TWO", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("THREE", "CLUBS"), ("THREE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("FOUR", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("FIVE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("SIX", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("THREE", "CLUBS"), ("FOUR", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("FIVE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("SIX", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("SEVEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("THREE", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("FOUR", "CLUBS"), ("FOUR", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("FIVE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("SIX", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("FOUR", "CLUBS"), ("FIVE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("SIX", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("SEVEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FOUR", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("FIVE", "CLUBS"), ("FIVE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("SIX", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("FIVE", "CLUBS"), ("SIX", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("SEVEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("FIVE", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("SIX", "CLUBS"), ("SIX", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("SIX", "CLUBS"), ("SEVEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SIX", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("SEVEN", "CLUBS"), ("SEVEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("SEVEN", "CLUBS"), ("EIGHT", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("SEVEN", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("EIGHT", "CLUBS"), ("EIGHT", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("EIGHT", "CLUBS"), ("NINE", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("EIGHT", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("NINE", "CLUBS"), ("NINE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("NINE", "CLUBS"), ("TEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("NINE", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("TEN", "CLUBS"), ("TEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("TEN", "CLUBS"), ("JACK", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("TEN", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("JACK", "CLUBS"), ("JACK", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("JACK", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("JACK", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("JACK", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("JACK", "CLUBS"), ("QUEEN", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("JACK", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("JACK", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("QUEEN", "CLUBS"), ("QUEEN", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("QUEEN", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("QUEEN", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("QUEEN", "CLUBS"), ("KING", "CLUBS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("QUEEN", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("KING", "CLUBS"), ("KING", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("KING", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)

    hand = tuple(sorted([("ACE", "CLUBS"), ("ACE", "HEARTS")]))
    unique_combinations.add(hand)
    hand = tuple(sorted([("KING", "CLUBS"), ("ACE", "CLUBS")]))
    unique_combinations.add(hand)

    return unique_combinations

def simulate_preflop_odds(num_simulations=250000):
    unique_combinations = num_of_calculations()
    # for card1 in self.deck.cards:
    #     for card2 in self.deck.cards:
    #         if card1 != card2:
    #             print(card1.rank)
    #             print(card1.rank.name)
    #             print(card1.suit)
    #             print(card1.suit.name)
    #             hand = tuple(sorted([(card1.rank.name, card1.suit.name), (card2.rank.name, card2.suit.name)]))
    #             unique_combinations.add(hand)

    combinations_to_simulate = list(unique_combinations)
    
    with Pool(cpu_count()) as pool:
        results = pool.starmap(simulate_single_combination, [(card1, card2, num_simulations) for card1, card2 in combinations_to_simulate])

    with sqlite3.connect('poker_odds_newShuffle.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO Preflop (
                card1, card2, win_rate, high_card, one_pair, two_pair, three_of_a_kind,
                straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', results)
        conn.commit()

def card_to_string(card):
    return f"{card.rank.name} of {card.suit.name}"

def card_from_tuple(card_tuple):
    rank, suit = card_tuple
    return Card(Suit[suit], Value[rank])

def simulate_single_combination(card1_tuple, card2_tuple, num_simulations=250000):
    card1 = card_from_tuple(card1_tuple)
    card2 = card_from_tuple(card2_tuple)
    game = PokerGame([Player("Alice", 10000), Player("Bob", 10000)])  # Temporary game instance for simulation
    wins = 0
    hand_counts = {
        "High Card": 0,
        "One Pair": 0,
        "Two Pair": 0,
        "Three of a Kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Four of a Kind": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for _ in range(num_simulations):
        game.reset_game()
        game.deal_specific_cards(card1, card2)
        game.deal_remaining_cards()
        if game.showdown() == game.players[0]:
            wins += 1
            hand_counts[game.player_hand] += 1

    win_rate = (wins / num_simulations) * 100
    hand_percentages = {hand: (count / num_simulations) * 100 for hand, count in hand_counts.items()}
    return (
        card_to_string(card1),
        card_to_string(card2),
        win_rate,
        hand_percentages["High Card"],
        hand_percentages["One Pair"],
        hand_percentages["Two Pair"],
        hand_percentages["Three of a Kind"],
        hand_percentages["Straight"],
        hand_percentages["Flush"],
        hand_percentages["Full House"],
        hand_percentages["Four of a Kind"],
        hand_percentages["Straight Flush"],
        hand_percentages["Royal Flush"]
    )

def main():
    player1 = Player("Alice", 10000)
    player2 = Player("Bob", 10000)
    game = PokerGame([player1, player2])
    create_hands_table()
    simulate_preflop_odds()

if __name__ == "__main__":
    main()