class State:
    board = [[0 for col in range(19)] for row in range(19)]
    actions = []
    bestAction = ()

    def __init__(self):
        self.board = [[0 for col in range(19)] for row in range(19)]
        self.actions = []
        self.bestAction = ()

    def terminalTest(self):
        if self.actions == []:
            return True
        else:
            return False