# TODO: Jeg skal gøre så man kan opgradere sig til at være hurtigere(vel) i Player
# TODO: Skal kunne skyde
# TODO: En modstander skal på skærmen
import pygame
from player import Player
import time

# jeg skal lave et spil hvor man skal styre at et rumskib flyver lige

pygame.init()
width = 800
height = 600
# WINDOW
win = pygame.display.set_mode([width, height])
# 'TITLE'
pygame.display.set_caption('Shooting Game')


def login():
    color = pygame.Color('black')

    username_rect = pygame.Rect(width // 4, height // 4, 140, 32)
    title_font = pygame.font.Font('freesansbold.ttf', 50)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    win.fill((0, 0, 0))
                    pygame.display.update()
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        win.fill((255, 255, 255))

        string = title_font.render('Login', True, (255, 132, 27))
        username = base_font.render(user_text, True, (0, 0, 0))
        win.blit(string, (width // 2 - 70, 50))
        win.blit(username, (width // 4, height // 4))

        pygame.draw.rect(win, color, username_rect, 2)
        pygame.display.flip()
        clock.tick(60)
    print(user_text)


def redraw_window(win, player):
    bg = pygame.image.load("stars.png")
    win.blit(bg, (0, 0))
    player.draw(win)
    pygame.display.update()


def main():
    # login()
    run = True
    p = Player(width//2 - 70//2, height - 71, 'space-invaders.png')
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        p.move()
        redraw_window(win, p)


main()
