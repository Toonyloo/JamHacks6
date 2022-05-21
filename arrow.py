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
    
    def shoot(self, angle, power): # Takes in an angle from 0-360, and a power from 0 to 1
        self.total_vel = Consts.MAX_ARROW_SPEED * power
        self.y_vel = math.sin(math.radians(angle)) * self.total_vel * -1
        self.x_vel = math.cos(math.radians(angle)) * self.total_vel
        self.attached = False