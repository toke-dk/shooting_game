import pygame


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, win):
        self.img = pygame.image.load('space-invaders.png')
        self.img = pygame.transform.scale(self.img, (70, 70))
        win.blit(self.img, (self.x, self.y))