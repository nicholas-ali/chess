import chess

def evaluate(board):
    fen  = board.board_fen()
    score = 200*(fen.count("K") - fen.count("k"))
    score += 9*(fen.count("Q") - fen.count("q"))
    score += 5*(fen.count("R") - fen.count("r"))
    score += 3*(fen.count("B") - fen.count("b") + fen.count("N") - fen.count("n"))
    score += 1*(fen.count("P") - fen.count("p"))
    return score


