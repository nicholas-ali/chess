import pygame
import pygame_gui
import chess

board = chess.Board()




pygame.init()

wp = pygame.image.load("images/wp.png")
wp = pygame.transform.scale(wp, (50, 50))
wr = pygame.image.load("images/wr.png")
wr = pygame.transform.scale(wr, (50, 50)) 
wb = pygame.image.load("images/wb.png")
wb = pygame.transform.scale(wb, (50, 50))
wn = pygame.image.load("images/wn.png")
wn = pygame.transform.scale(wn, (50, 50))


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((400, 400))

background = pygame.Surface((400, 400))
background.fill(pygame.Color('#ffffff'))

manager = pygame_gui.UIManager((400, 400))

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
        



for i in board.fen():
    cr = 

clock = pygame.time.Clock()
is_running = True
currentSqr  = None


while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            currentSqr = int(x/50) + 10*(7-int(y/50)) - (7-int(y/50))*2
            print(chess.square_name(currentSqr))
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
