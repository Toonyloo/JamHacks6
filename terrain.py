import pygame
from constants import Consts, Images

class Ground:
    def __init__(self, x, y, width, height, tag = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tag = tag
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 0)

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Goal, self).__init__()
        self.x = x
        self.y = y
        self.image = Images.FLAG
        self.rect = pygame.Rect(self.x, self.y - Consts.FLAG_H, Consts.FLAG_W, Consts.FLAG_H)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y - Consts.FLAG_H))