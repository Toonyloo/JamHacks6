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

class Door:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.closed = True
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        if self.closed:
            pygame.draw.rect(screen, (120, 0, 255), self.rect)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, vert, door):
        super(Button, self).__init__()
        self.x = x
        self.y = y
        self.pressed = False
        self.vertical = vert
        self.door = door
        if self.vertical:
            self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_W, Consts.BUTTON_L)
        else:
            self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_L, Consts.BUTTON_W)
    
    def press(self):
        if not self.pressed:
            self.door.closed = False
            if self.vertical:
                self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_W - 30, Consts.BUTTON_L)
            else:
                self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_L, Consts.BUTTON_W - 30)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
