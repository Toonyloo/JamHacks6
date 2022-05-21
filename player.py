import pygame
from constants import Consts, Images

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.x = 300
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
    
    def terrain_collision(self, terrain):
        x = self.x + self.x_vel
        y = self.y + self.y_vel
        
        # TODO HELP ME JEFFERY
        # FIX THIS SHIT
        x_between = terrain.x - Consts.PLAYER_W < x < terrain.x + terrain.width
        y_between = terrain.y - Consts.PLAYER_H < y < terrain.y + terrain.height
        # Colllision with floor
        if y + Consts.PLAYER_H > terrain.y and x_between:
            self.grounded = True
            self.y = terrain.y - Consts.PLAYER_H

        # Collision with right side of wall
        if x_between and y_between:
            self.x_vel = 0

        # # Colliion with left side of wall
        # if x + Consts.PLAYER_W > terrain.x and y_between:
        #     self.x_vel = 0
        
        # Collsion with ceiling
        if y < terrain.y + terrain.height and x_between:
            self.y_vel = 0
