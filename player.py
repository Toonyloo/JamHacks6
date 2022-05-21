import pygame
from constants import Consts, Images

class Player:
    def __init__(self, spawn):
        self.x, self.y = spawn
        self.x_vel = 0
        self.y_vel = 0
        self.grounded = 0
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
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.grounded > 1:
                    self.y_vel = -Consts.JUMP_STR

    def handle_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel
        if self.y_vel != 0:
            self.grounded = 0
        else:
            self.grounded += 1
        self.y_vel += Consts.GRAVITY
    
    def terrain_collision_top(self, terrain): # Colliding with top of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.PLAYER_W
        bottom_y = top_y + Consts.PLAYER_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if top_y < ttop_y < bottom_y and self.x + Consts.PLAYER_W > tleft_x and self.x < tright_x:
            return True
        return False
    
    def terrain_collision_bottom(self, terrain): # Colliding with bottom of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.PLAYER_W
        bottom_y = top_y + Consts.PLAYER_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if top_y < tbottom_y < bottom_y and self.x + Consts.PLAYER_W > tleft_x and self.x < tright_x:
            return True
        return False
    
    def terrain_collision_left(self, terrain): # Colliding with left of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.PLAYER_W
        bottom_y = top_y + Consts.PLAYER_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if left_x < tleft_x < right_x and self.y < tbottom_y and self.y + Consts.PLAYER_H > ttop_y:
            return True
        return False
    
    def terrain_collision_right(self, terrain): # Colliding with top of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.PLAYER_W
        bottom_y = top_y + Consts.PLAYER_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if right_x > tright_x > left_x and self.y < tbottom_y and self.y + Consts.PLAYER_H > ttop_y:
            return True
        return False
    


    def terrain_collision(self, terrain):

        if self.terrain_collision_left(terrain) or self.terrain_collision_right(terrain):
            self.x_vel = 0

        if self.terrain_collision_top(terrain):
            self.y_vel = 0

        if self.terrain_collision_bottom(terrain):
            self.y_vel = 0

