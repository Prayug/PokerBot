class GameNode:
    def __init__(self, info_set):
        self.info_set = info_set
        self.regrets = {}
        self.strategy = {}
        self.strategy_sum = {}
        self.actions = ['fold', 'call', 'raise']

        for action in self.actions:
            self.regrets[action] = 0
            self.strategy[action] = 1 / len(self.actions)
            self.strategy_sum[action] = 0

    def get_strategy(self):
        normalizing_sum = sum(self.strategy.values())
        if normalizing_sum > 0:
            for action in self.actions:
                self.strategy[action] /= normalizing_sum
        else:
            for action in self.actions:
                self.strategy[action] = 1 / len(self.actions)

        return self.strategy

    def update_strategy_sum(self):
        for action in self.actions:
            self.strategy_sum[action] += self.strategy[action]

    def get_average_strategy(self):
        normalizing_sum = sum(self.strategy_sum.values())
        average_strategy = {}
        if normalizing_sum > 0:
            for action in self.actions:
                average_strategy[action] = self.strategy_sum[action] / normalizing_sum
        else:
            for action in self.actions:
                average_strategy[action] = 1 / len(self.actions)

        return average_strategy
