import chess
import engine

board = chess.BaseBoard()

squares = chess.SquareSet()

for i in range(1, 7):
    for sqaure in board.pieces(i, False):
        squares = squares.union(board.attacks(sqaure))


print(squares)