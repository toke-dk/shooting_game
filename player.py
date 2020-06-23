import pygame
from laser import Laser


# her skal den aktivere laser class hvis der bliver trykket pil op


class Player:
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y
        self.vel = 4
        self.width = width
        self.height = height
        self.img = img

    def draw(self, win):
        # think it is wrong here
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (self.width, self.height))
        win.blit(img, (self.x, self.y))

    # skal ikke have win
    def move(self, win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            # if keys[pygame.K_UP]:
            #     print('Key_UP')
            #     l.draw(win)
        self.update(win)

    # det hakker fordi den blit

    def update(self, win):
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (self.width, self.height))
        win.blit(img, (self.x, self.y))