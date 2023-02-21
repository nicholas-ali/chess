import chess
import engine

board = chess.Board()
board.push_san("e4")
board.push_san("d5")
moves = board.legal_moves
toMoves = list()
for move in moves:
    toMoves.append(move.to_square)

bitMoves = chess.SquareSet(toMoves)

squares = chess.SquareSet()

intersections = list()
for i in range(1, 7):
    for sqaure in board.pieces(i, False):
        squares = squares.union(board.attacks(sqaure))
        squares = squares.intersection(bitMoves)

print(toMoves)
print(list(squares))
for square in squares:
    print(square)
    intersections.append(toMoves.index(sqaure))
    toMoves.remove(square)
count = 0
for i in range(moves):
    if i in intersections:
        moves.pop(i-count)
        count +=1
print(moves)
