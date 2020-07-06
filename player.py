import pygame
from laser import Laser
from laser import Laser


# her skal den aktivere laser class hvis der bliver trykket pil op


class Player:
    def __init__(self, x, y, width, height, img, rotation):
        self.x = x
        self.y = y
        self.vel = 15
        self.width = width
        self.height = height
        self.img = img
        self.rotation = rotation

    def draw(self, win):
        # think it is wrong here
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (self.width, self.height))
        img = pygame.transform.rotate(img, self.rotation)
        win.blit(img, (self.x, self.y))

    # skal ikke have win
    def move(self, win):
        self.l = Laser(self.x, self.y)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_SPACE]:
            print('presesd space')
            self.l.draw(win)
            # if keys[pygame.K_UP]:
            #     print('Key_UP')
            #     l.draw(win)
        self.update(win)

    def update(self, win):
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (self.width, self.height))
        img = pygame.transform.rotate(img, self.rotation)
        win.blit(img, (self.x, self.y))