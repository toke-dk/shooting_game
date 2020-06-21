import pygame

pygame.init()
width = 800
height = 600
# WINDOW
win = pygame.display.set_mode([width, height])
# 'TITLE'
pygame.display.set_caption('Shooting Game')
base_font = pygame.font.Font(None, 32)


def main():
    user_text = ''
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                user_text += event.unicode
        win.fill((255, 255, 255))
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        win.blit(text_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)


main()