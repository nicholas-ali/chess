import pygame
import pygame_gui
import chess


def drawBoard():
    fen = board.fen().replace("/", "")
    xval = 0
    yval = 0
    for i in fen:
        if i.isnumeric():
            xval += int(i)-1
        elif i == "p":
            background.blit(bp, (xval*50, yval*50))
        elif i == "r":
            background.blit(br, (xval*50, yval*50))
        elif i == "b":
            background.blit(bb, (xval*50, yval*50))
        elif i == "n":
            background.blit(bn, (xval*50, yval*50))
        elif i == "q":
            background.blit(bq, (xval*50, yval*50))
        elif i == "k":
            background.blit(bk, (xval*50, yval*50))
        elif i == "P":
            background.blit(wp, (xval*50, yval*50))
        elif i == "R":
            background.blit(wr, (xval*50, yval*50))
        elif i == "B":
            background.blit(wb, (xval*50, yval*50))
        elif i == "N":
            background.blit(wn, (xval*50, yval*50))
        elif i == "Q":
            background.blit(wq, (xval*50, yval*50))
        elif i == "K":
            background.blit(wk, (xval*50, yval*50))
        elif i == " ":
            break
        if xval == 7:
            xval = 0
            yval += 1
        else:
            xval += 1


def updateScreen():
    for i in range(0, 8):
        for x in range(0, 8):
            if i%2:
                if x%2:
                    pygame.draw.rect(background, (238,238,210), (50*i, 50*x, 50, 50))
                else:
                    pygame.draw.rect(background, (118,150,86), (50*i, 50*x, 50, 50))
            else:
                if x%2:
                    pygame.draw.rect(background, (118,150,86), (50*i, 50*x, 50, 50))
                else:
                    pygame.draw.rect(background, (238,238,210), (50*i, 50*x, 50, 50))
    drawBoard()

pygame.init()
wp = pygame.image.load("images/wp.png")
wp = pygame.transform.scale(wp, (50, 50))
wr = pygame.image.load("images/wr.png")
wr = pygame.transform.scale(wr, (50, 50)) 
wb = pygame.image.load("images/wb.png")
wb = pygame.transform.scale(wb, (50, 50))
wn = pygame.image.load("images/wn.png")
wn = pygame.transform.scale(wn, (50, 50))
wq = pygame.image.load("images/wq.png")
wq = pygame.transform.scale(wq, (50, 50))
wk = pygame.image.load("images/wk.png")
wk = pygame.transform.scale(wk, (50, 50))
bp = pygame.image.load("images/bp.png")
bp = pygame.transform.scale(bp, (50, 50))
br = pygame.image.load("images/br.png")
br = pygame.transform.scale(br, (50, 50)) 
bb = pygame.image.load("images/bb.png")
bb = pygame.transform.scale(bb, (50, 50))
bn = pygame.image.load("images/bn.png")
bn = pygame.transform.scale(bn, (50, 50))
bq = pygame.image.load("images/bq.png")
bq = pygame.transform.scale(bq, (50, 50))
bk = pygame.image.load("images/bk.png")
bk = pygame.transform.scale(bk, (50, 50))


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((400, 400))
background = pygame.Surface((400, 400))
background.fill(pygame.Color('#ffffff'))
manager = pygame_gui.UIManager((400, 400))

board = chess.Board()
clock = pygame.time.Clock()
is_running = True
currentSqr  = None
curPiece = None
curMove = ""

updateScreen()

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            currentSqr = int(x/50) + 10*(7-int(y/50)) - (7-int(y/50))*2
            curPiece = board.piece_at(currentSqr)
            if len(curMove):
                if not curMove == chess.square_name(currentSqr):
                    curMove = curMove + chess.square_name(currentSqr)
            elif curPiece:
                curMove = chess.square_name(currentSqr)
            if len(curMove) == 4:
                if (chess.Move.from_uci(curMove) in board.legal_moves):
                    board.push(chess.Move.from_uci(curMove))
                    updateScreen()
                curMove = ""
                if curPiece:
                    curMove = chess.square_name(currentSqr)
            if board.is_game_over():
                if board.outcome().winner:
                    print("White Wins")
                elif board.outcome().winner == False:
                    print("Black Wins")
                else:
                    print("Draw")
                board.reset()
                updateScreen()
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
