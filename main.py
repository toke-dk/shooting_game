import pygame

width = 800
height = 600
# WINDOW
win = pygame.display.set_mode((width, height))
# 'TITLE'
pygame.display.set_caption('Shooting Game')


def redraw_window(win):
    # White
    win.fill((255, 255, 255))
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        redraw_window(win)


main()