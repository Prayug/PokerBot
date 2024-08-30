import eel
from Player import Player
from Game import PokerGame
from AI_levels.AILevel1 import AIPlayerLevel1
from AI_levels.AILevel2 import AIPlayerLevel2


eel.init('web')

player1 = Player("Player", 10000)
player2 = AIPlayerLevel2("AI", 10000)  # AI player
game = PokerGame([player1, player2], big = 100)
cards_dealt = False
preflop = True

@eel.expose
def get_initial_state():
    return game.get_game_state()

@eel.expose
def deal_cards():
    global cards_dealt, preflop
    if not cards_dealt:
        game.collect_blinds()
        game.deal_cards()
        cards_dealt = True
        preflop = True
    return game.get_game_state()

@eel.expose
def get_best_hand():
    best_hand, hand_type = game.get_best_hand(player1)
    return {
        "best_hand": best_hand,
        "hand_type": hand_type
    }

@eel.expose
def collect_bets(action, raise_amount=None):
    if action == "check":
        if not preflop:
            print(game.players[1].chips)
            print("check collecting again")
            game.collect_bets(action)
            print(game.players[1].chips)
        else:
            print("check preflop")
            ai_decision = game.players[1].make_decision_pre()
            if ai_decision >= 55:
                game.players[1].isRaise = True
                game.player_raise(game.players[1], 3 * game.big_blind)
            else:
                game.finish_blinds()
                game.collect_bets("check")
    elif action == "raise" and raise_amount is not None:
        print(game.players[1].chips)
        print("raise collecting again")
        game.collect_bets(action, raise_amount)
        print(game.players[1].chips)
    elif action == "ai_action":
        print(game.players[1].chips)
        if game.players[1].isRaise:
            ai_decision = game.players[1].make_decision_pre()
            if ai_decision >= 45 and ai_decision < 55:
                game.ai_call(game.players[1], "raise")
            elif ai_decision <= 55:
                game.players[1].isRaise = True
                game.player_raise(game.players[1], 3 * game.big_blind)
            else:
                game.players[1].fold_hand()
                game.players[0].chips += game.pot
                game.pot = 0
                game.log.append(f"{game.players[0].name} wins the pot.")
                game.winner_paid = True
        print(game.players[1].chips)
    elif action == "call":
        print(game.players[1].chips)
        print("call collecting again")
        game.collect_bets(action)
        print(game.players[1].chips)

    return game.get_game_state()


@eel.expose
def deal_community_cards(number):
    game.deal_community_cards(number)
    return game.get_game_state()

@eel.expose
def showdown():
    game.showdown()
    return game.get_game_state()

@eel.expose
def reset_game():
    global cards_dealt, preflop
    game.reset_game()
    cards_dealt = False
    preflop = False
    return game.get_game_state()

@eel.expose
def fold():
    global cards_dealt, preflop
    game.fold()
    cards_dealt = False
    preflop = False
    return game.get_game_state()

eel.start('index.html', size=(1000, 600))