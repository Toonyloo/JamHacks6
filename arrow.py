import pygame
import math
from constants import Consts, Images

class Arrow:
    def __init__(self, p): # initiates with a Player class
        self.player = p
        self.x = self.player.x
        self.y = self.player.y
        self.xprev = 0
        self.yprev = 0
        self.x_vel = 0
        self.y_vel = 0
        self.total_vel = 0
        self.grounded = True
        self.attached = True

    def handle_movement(self):
        if self.attached:
            self.yprev = self.y
            self.xprev = self.x
            self.x = self.player.x 
            self.y = self.player.y
        else:
            self.xprev = self.x
            self.yprev = self.y
            self.x += self.x_vel
            self.y += self.y_vel
            self.y_vel += Consts.GRAVITY
    
    def attach(self):
        if self.player.x + Consts.PLAYER_W >= self.x and self.player.x <= self.x + Consts.ARROW_W and self.player.y <= self.y + Consts.ARROW_H and self.player.y + Consts.PLAYER_H >= self.y:
            self.attached = True
    
    def shoot(self, mouse_pos): # Takes in an angle from 0-360
        diff_x = mouse_pos[0] - (self.player.x + Consts.PLAYER_W / 2)
        diff_y = (self.player.y + Consts.PLAYER_H / 2) -  mouse_pos[1]
        power = math.sqrt(diff_x ** 2 + diff_y ** 2)
        if diff_x >= 0:
            angle = math.atan(diff_y / diff_x)
        else:
            angle = math.atan(diff_y / diff_x) + math.pi
        self.total_vel = power * 0.05
        self.y_vel = math.sin(angle) * self.total_vel * -1
        self.x_vel = math.cos(angle) * self.total_vel
        self.attached = False
    
    def draw(self, screen):
        if not self.attached:
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10)

    def terrain_collision_top(self, terrain): # Colliding with top of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.ARROW_W
        bottom_y = top_y + Consts.ARROW_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if ttop_y > self.yprev and ttop_y < bottom_y and self.x + Consts.ARROW_W > tleft_x and self.x < tright_x:
            return True
        return False
    
    def terrain_collision_bottom(self, terrain): # Colliding with bottom of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.ARROW_W
        bottom_y = top_y + Consts.ARROW_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if tbottom_y < self.yprev and top_y < tbottom_y and self.x + Consts.ARROW_W > tleft_x and self.x < tright_x:
            return True
        return False
    
    def terrain_collision_left(self, terrain): # Colliding with left of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.ARROW_W
        bottom_y = top_y + Consts.ARROW_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if tleft_x > self.xprev + Consts.ARROW_W and tleft_x < right_x and self.y < tbottom_y and self.y + Consts.ARROW_H > ttop_y:
            return True
        return False
    
    def terrain_collision_right(self, terrain): # Colliding with top of terrain
        left_x = self.x + self.x_vel
        top_y = self.y + self.y_vel
        right_x = left_x + Consts.ARROW_W
        bottom_y = top_y + Consts.ARROW_H

        tleft_x = terrain.x
        tright_x = tleft_x + terrain.width
        ttop_y = terrain.y
        tbottom_y = ttop_y + terrain.height

        if tright_x < self.xprev and tright_x > left_x and self.y < tbottom_y and self.y + Consts.ARROW_H > ttop_y:
            return True
        return False    

    def terrain_collision(self, terrain):

        if self.terrain_collision_left(terrain) or self.terrain_collision_right(terrain):
            if self.x_vel < 0:
                self.x_vel = -self.x_vel - min(Consts.COLLISION_LOSS, -self.x_vel - Consts.MIN_COLLISION_SPEED)
            else:
                self.x_vel = -self.x_vel + min(Consts.COLLISION_LOSS, self.x_vel - Consts.MIN_COLLISION_SPEED)

        if self.terrain_collision_top(terrain):
            self.y_vel = 0
            self.x_vel = 0

        if self.terrain_collision_bottom(terrain):
            self.y_vel = 0

    def swap(self):
        self.x, self.player.x = self.player.x, self.x
        self.y , self.player.y = self.player.y, self.y - (Consts.PLAYER_H - Consts.ARROW_H)
        self.xprev = self.x
        self.yprev = self.y
        