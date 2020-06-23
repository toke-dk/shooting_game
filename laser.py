import pygame


class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        laser = pygame.image.load('laser.png')
        pygame.transform.scale(laser, (5, 10))
        win.blit(laser, (self.x, self.y))
        print('has drewn')

    def move(self):
        pass
