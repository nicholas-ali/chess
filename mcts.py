import numpy as np
from conversion import *

c_puct = 2
c_puct_decayRate = 0.00001


class Action:
    __slots__ = "Q", "N", "V", "R", "state,", "prev_states"

class Node:
    __slots__ = "board", "move", "children", "parents", "states", "action"

    def __init__ (self, move, board, parents):
        self.board = board
        # self.board.stack = 
        self.children = []
        self.parents = parents
        self.states = np.append(np.array(parents), self)
