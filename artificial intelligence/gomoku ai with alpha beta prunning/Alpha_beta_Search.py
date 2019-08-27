import Eval
import copy
import pygame

def update(state, i, j, p):
    state.actions = []
    state.board[i][j] = p
    for i in range(0, 19):
        for j in range(0, 19):
            if state.board[i][j] != 0:
                for k in range(i-4, i+5):
                    for l in range(j-4, j+5):
                        check = 0
                        for action in state.actions:
                            if action == (k, l):
                                check = 1
                        if check == 0 and k >= 0 and k <= 18 and l >= 0 and l <= 18:
                            if state.board[k][l] == 0:
                                state.actions.append((k, l))
    return state

def alphaBetaSearch(state):
    d = 0
    deadline = 0
    pygame.time.set_timer(deadline +1, 100000)
    while deadline == 0:
        d -= 1
        v = minValue(state, -9999, +9999, d)
        for event in pygame.event.get():
            if event.type == deadline + 1:
                deadline = 1
    return state.bestAction

def maxValue(state, a, b, d):
    if  d >= 0:
        return Eval.utility(state.board, 2)
    v = -9999
    for action in state.actions:
        temp_state = copy.deepcopy(state)
        update(temp_state, action[0], action[1], 1)
        vchild = minValue(temp_state, a, b, d + 1)
        if v < vchild:
            state.bestAction = action
            v = vchild
        if v >= b:
            return  v
        a = max(a, v)
    return v

def minValue(state, a, b, d):
    if  d >= 0:
        return Eval.utility(state.board, 1)
    v = 9999
    for action in state.actions:
        temp_state = copy.deepcopy(state)
        update(temp_state, action[0], action[1], 2)
        vchild = maxValue(temp_state, a, b, d + 1)
        if v > vchild:
            state.bestAction = action
            v = vchild
        if v <= a:
            return v
        b = min(b, v)
    return v
