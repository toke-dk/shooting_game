import pygame
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


def main():
    login()
    bg = pygame.image.load("stars.png")
    run = True
    win.blit(bg, (0, 0))
    img = pygame.image.load('space-invaders.png')
    img = pygame.transform.scale(img, (70, 70))
    win.blit(img, (width/2, height - 71))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


main()
