import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 800))

background = pygame.Surface((800, 800))
background.fill(pygame.Color('#ffffff'))

manager = pygame_gui.UIManager((800, 800))

for i in range(0, 8):
    for x in range(0, 8):
        if i%2:
            if x%2:
                pygame.draw.rect(background, (238,238,210), (100*i, 100*x, 100, 100))
            else:
                pygame.draw.rect(background, (118,150,86), (100*i, 100*x, 100, 100))
        else:
            if x%2:
                pygame.draw.rect(background, (118,150,86), (100*i, 100*x, 100, 100))
            else:
                pygame.draw.rect(background, (238,238,210), (100*i, 100*x, 100, 100))
        
Bishop = pygame.image.load("blackBishop.png")
Bishop = pygame.transform.scale(Bishop, (100, 100))

background.blit(Bishop, (100, 100))

background.blit(Bishop, (200, 100))

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
