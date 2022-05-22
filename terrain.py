import pygame
from constants import Consts, Images, Sfx

class Ground:
    def __init__(self, x, y, width, height, tag = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tag = tag
        self.rect = pygame.Rect(x, y, width, height)
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.blit(Images.FLOOR, (0, 0))
    
    def draw(self, screen):
        screen.blit(self.surf, (self.x, self.y))

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
        self.image = pygame.transform.scale(Images.DOOR, (self.width, self.height))
    
    def draw(self, screen):
        if self.closed:
            screen.blit(self.image, (self.x, self.y))

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, vert, flipped, door):
        super(Button, self).__init__()
        self.x = x
        self.y = y
        self.pressed = False
        self.vertical = vert  # Vertical means left or right wall
        self.door = door
        self.flipped = flipped  # Flipped means on a right wall or bottom
        if self.vertical:
            self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_W, Consts.BUTTON_L)
        else:
            self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_L, Consts.BUTTON_W)
    
    def press(self):
        if not self.pressed:
            self.door.closed = False
            Sfx.BUTTON.play()
            if self.vertical:
                if not self.flipped:
                    self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_W - 30, Consts.BUTTON_L)
                else:
                    self.rect = pygame.Rect(self.x + 30, self.y, Consts.BUTTON_W - 30, Consts.BUTTON_L)
            else:
                if not self.flipped:
                    self.rect = pygame.Rect(self.x, self.y, Consts.BUTTON_L, Consts.BUTTON_W - 30)
                else:
                    self.rect = pygame.Rect(self.x, self.y + 30, Consts.BUTTON_L, Consts.BUTTON_W - 30)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        if self.vertical:
            if not self.flipped:
                pygame.draw.rect(screen, (0), pygame.Rect(self.x, self.y - 10, Consts.BUTTON_W - 35, Consts.BUTTON_L + 20))
            else:
                pygame.draw.rect(screen, (0), pygame.Rect(self.x + 35, self.y - 10, Consts.BUTTON_W - 35, Consts.BUTTON_L + 20))
        else:
            if not self.flipped:
                pygame.draw.rect(screen, (0), pygame.Rect(self.x - 10, self.y, Consts.BUTTON_L + 20, Consts.BUTTON_W - 35))
            else:
                pygame.draw.rect(screen, (0), pygame.Rect(self.x - 10, self.y + 35, Consts.BUTTON_L + 20, Consts.BUTTON_W - 35))