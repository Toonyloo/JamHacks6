import pygame

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

class Goal:
    def __init__(self, x, y):
        pass