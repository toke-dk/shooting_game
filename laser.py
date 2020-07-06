import pygame


class Laser:
    # add x and y as parameters
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        laser_img = pygame.image.load('laser.png')
        laser_img = pygame.transform.scale(laser_img, (30, 60))
        win.blit(laser_img, (self.x, self.y))
        print('has drewn')
        self.update(win)

    def update(self, win):
        laser_img = pygame.image.load('laser.png')
        laser_img = pygame.transform.scale(laser_img, (30, 60))
        win.blit(laser_img, (self.x, self.y))
        pygame.display.update()