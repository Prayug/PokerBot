from GameNode import GameNode

class CFRTrainer:
    def __init__(self, game):
        self.game = game
        self.node_map = {}

    def train(self, iterations):
        utility = 0
        for i in range(iterations):
            utility += self.cfr(self.game, 1, 1)
        return utility

    def cfr(self, game, p0, p1):
        if game.is_terminal():
            return game.get_payoff()

        info_set = game.get_info_set()
        if info_set not in self.node_map:
            self.node_map[info_set] = GameNode(info_set)

        node = self.node_map[info_set]
        strategy = node.get_strategy()
        node.update_strategy_sum()

        util = {}
        node_util = 0
        for action in node.actions:
            next_game = game.get_next_game(action)
            if game.is_player0_turn():
                util[action] = -self.cfr(next_game, p0 * strategy[action], p1)
            else:
                util[action] = -self.cfr(next_game, p0, p1 * strategy[action])
            node_util += strategy[action] * util[action]

        for action in node.actions:
            regret = util[action] - node_util
            node.regrets[action] += (p1 if game.is_player0_turn() else p0) * regret

        return node_util
