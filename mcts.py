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
        
def evaluate(board):
    if board.is_checkmate(): return 1
    else: return -1


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


class MCT():
    __slots__ = ["prev_node", "chain", "root_node", "model", "sims"]

    def __init__ (self, model, board, parents):
        self.board = board
        self.model = model
        self.chain = []
        self.createRootNode(board, parents)
        self.sims = 0

    def createRootNode(self, board, parents):
        
