import pygame
import math
from constants import Consts, Images

class Arrow:
    def __init__(self, p): # initiates with a Player class
        self.player = p
        self.x = self.player.x
        self.y = self.player.y
        self.x_vel = 0
        self.y_vel = 0
        self.total_vel = 0
        self.grounded = True
        self.attached = True

    def handle_movement(self):
        if self.attached:
            self.x = self.player.x 
            self.y = self.player.y
        else:
            self.x += self.x_vel
            self.y += self.y_vel
            self.y_vel += Consts.GRAVITY
    
    def attach(self):
        self.attached = True
    
    def shoot(self, mouse_pos): # Takes in an angle from 0-360
        diff_x = mouse_pos[0] - (self.player.x + Consts.PLAYER_W / 2)
        diff_y = (self.player.y + Consts.PLAYER_H / 2) -  mouse_pos[1]
        
        print(diff_x, diff_y)
        power = math.sqrt(diff_x ** 2 + diff_y ** 2)
        if diff_x >= 0:
            angle = math.atan(diff_y / diff_x)
        else:
            angle = math.atan(diff_y / diff_x) + math.pi
        print(power, math.degrees(angle))
        self.total_vel = power * 0.05
        self.y_vel = math.sin(angle) * self.total_vel * -1
        self.x_vel = math.cos(angle) * self.total_vel
        self.attached = False
    
    def draw(self, screen):
        if not self.attached:
            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 10)