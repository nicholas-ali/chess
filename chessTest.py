import chess
import engine

board = chess.Board()
moves = board.legal_moves
toMoves = list()
for move in moves:
    toMoves.append(move.to_square)

bitMoves = chess.SquareSet(toMoves)
print(bitMoves)

squares = chess.SquareSet()

for i in range(1, 7):
    for sqaure in board.pieces(i, False):
        squares = squares.union(board.attacks(sqaure))

