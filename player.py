import pygame
from constants import Consts, Images

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.x = 0
        self.y = Consts.HEIGHT - Consts.PLAYER_H 
        self.x_vel = 0
        self.y_vel = 0
        self.grounded = True
        self.image = Images.PLAYER
        self.rect = pygame.Rect(self.x, self.y, Consts.PLAYER_W, Consts.PLAYER_H)
    
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, Consts.PLAYER_W, Consts.PLAYER_H)
        screen.blit(self.image, (self.x, self.y))
    
    def handle_inputs(self, keys, events):
        self.x_vel = 0
        if keys[pygame.K_a]:
            self.x_vel -= Consts.PLAYERSPEED
        if keys[pygame.K_d]:
            self.x_vel += Consts.PLAYERSPEED
        if keys[pygame.K_w] and self.grounded:
            self.y_vel = -Consts.JUMP_STR
            self.grounded = False
    
    def handle_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.grounded:
            self.y_vel = 0
        else:
            self.y_vel += Consts.GRAVITY
    
    def collide_floor(self, ground):
        if self.y + Consts.PLAYER_H + self.y_vel > ground.y:
            self.grounded = True
            self.y = ground.y - Consts.PLAYER_H