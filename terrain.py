import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Ground, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 0)
    