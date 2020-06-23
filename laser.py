import pygame


class Laser:
    # add x and y as parameters
    def __init__(self):
        pass

    def draw(self, win):
        laser_img = pygame.image.load('laser.png')
        laser_img = pygame.transform.scale(laser_img, (30, 60))
        win.blit(laser_img, (0, 0))
        print('has drewn')
        self.update(win)

    def update(self, win):
        laser_img = pygame.image.load('laser.png')
        laser_img = pygame.transform.scale(laser_img, (30, 60))
        win.blit(laser_img, (0, 0))
        pygame.display.update()