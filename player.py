import pygame


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.vel = 4

    def draw(self, win):
        self.img = pygame.image.load('space-invaders.png')
        self.img = pygame.transform.scale(self.img, (70, 70))
        win.blit(self.img, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel