import chess
import engine

board = chess.Board()
board.push_san("e4")
board.push_san("d5")
moves = board.legal_moves
toMoves = list()
for move in moves:
    toMoves.append(move.to_square)
moves = list(moves)
bitMoves = chess.SquareSet(toMoves)

squares = chess.SquareSet()

intersections = list()
for i in range(1, 7):
    for square in board.pieces(i, False):
        squares = squares.union(board.attacks(square))
        squares = squares.intersection(bitMoves)

print(toMoves)
print(list(squares))
for square in squares:
    print(square)
    intersections.append(toMoves.index(square))
    toMoves.remove(square)
print(moves)
for move in moves:
    if move.to_square in squares:
        moves.remove(move)
print(moves)
