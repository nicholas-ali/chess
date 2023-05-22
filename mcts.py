import numpy as np
from conversion import *

c_puct = 2
c_puct_decayRate = 0.00001


class Action:
    __slots__ = "Q", "N", "V", "R", "state,", "prev_states"

    def __init__ (self, state, move, parents):
        self.Q = 0
        self.N = 0
        self.V = 0
        self.R = 0
        self.state = state

        self.prev_states = [self.state]
        for node in parents:
            self.prev_states.append(node.board)

    def evaluate(self, P, Nl, v):
        P = P[0][self.moveidx]
        self.V = v
        return self.R/self.N + c_puct * P * (np.sqrt(Nl)/(1+ self.N))
        


class Node:
    __slots__ = "board", "move", "children", "parents", "states", "action"

    def __init__ (self, move, board, parents):
        self.board = board
        self.board.stack = []
        if move: self.move = move
        else: self.move = None
        self.children = []
        self.parents = parents
        self.states = np.append(np.array(parents), self)

        self.action = Action(self.board, self.move, self.states)
    def extend(self):
        if not self.children

