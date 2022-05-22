import pygame
from terrain import Ground, Goal, Button, Door
from constants import Fonts, Consts

class Test:
    def __init__(self):
        self.terrain = [Ground(0, 700, 1280, 20, "floor"),
               Ground(0, 0, 20, 720, "left wall"),
               Ground(1260, 0, 20, 720, "right wall"),
               Ground(400, 600, 200, 20, "platform"),
               Ground(300, 400, 200, 20, "platform"),
               Ground(0, 0, 1280, 20, "ceiling")]
        self.spawn = (50, 50)
        self.goal = Goal(700, 700)
        self.doors = []
        self.buttons = []
    
    def draw_text(self, screen):
        pass

class Lv1:
    def __init__(self):
        self.terrain = [Ground(0, 590, 320, 130),
               Ground(320, 460, 320, 260),
               Ground(640, 330, 320, 390),
               Ground(960, 200, 320, 520), 
               Ground(0, 0, 20, 720, "left wall"),
               Ground(1260, 0, 20, 720, "right wall"),
               Ground(0, 0, 1280, 20, "ceiling")]
        self.spawn = (20, 500)
        self.goal = Goal(1120, 200)
        self.doors = []
        self.buttons = []
    
    def draw_text(self, screen):
        txt = Fonts.TXT_FONT.render("Use A/D to move", True, (0, 140, 148))
        txt_rect = txt.get_rect(center=(Consts.WIDTH / 2, 80))
        screen.blit(txt, txt_rect)
        txt = Fonts.TXT_FONT.render("Press SPACE to jump", True, (0, 140, 148))
        txt_rect = txt.get_rect(center=(Consts.WIDTH / 2, 140))
        screen.blit(txt, txt_rect)

class Lv2:
    def __init__(self):
        self.terrain = [Ground(0, 700, 1280, 20, "floor"),
               Ground(0, 0, 20, 720, "left wall"),
               Ground(1260, 0, 20, 720, "right wall"),
               Ground(0, 0, 1280, 20, "ceiling"),
               Ground(400, 0, 20, 600),
               Ground(800, 300, 20, 420)]
        self.spawn = (20, 500)
        self.goal = Goal(1120, 700)
        self.doors = [Door(400, 580, 20, 120)]
        self.buttons = [Button(20, 120, True, False, self.doors[0])]
    
    def draw_text(self, screen):
        txt = Fonts.TXT_FONT.render("LEFT CLICK to shoot the arrow", True, (0, 140, 148))
        txt_rect = txt.get_rect(center=(Consts.WIDTH / 5 * 3, 80))
        screen.blit(txt, txt_rect)
        txt = Fonts.TXT_FONT.render("SHIFT to swap spaces with the arrow", True, (0, 140, 148))
        txt_rect = txt.get_rect(center=(Consts.WIDTH / 5 * 3, 130))
        screen.blit(txt, txt_rect)
        txt = Fonts.TXT_FONT.render("Walk to the accursed arrow to pick it up", True, (0, 140, 148))
        txt_rect = txt.get_rect(center=(Consts.WIDTH /5 * 3, 180))
        screen.blit(txt, txt_rect)

class Lv3:
    def __init__(self):
        self.terrain = [Ground(0, 0, 20, 720, "left wall"),
               Ground(1260, 0, 20, 720, "right wall"),
               Ground(0, 0, 1280, 20, "ceiling"),
               Ground(0, 600, 200, 120),
               Ground(300, 500, 200, 20),
               Ground(600, 500, 250, 20),
               Ground(1000, 500, 280, 320),
               Ground(1100, 200, 180, 20),
               Ground(650, 300, 225, 20),
               Ground(400, 300, 150, 20),
               Ground(0, 200, 300, 20)]
        self.spawn = (20, 500)
        self.goal = Goal(100, 200)
        self.doors = [Door(300, 380, 20, 120), Door(180, 0, 20, 200)]
        self.buttons = [Button(1100, 450, False, True, self.doors[0]), Button(1210, 30, True, True, self.doors[1])]

    def draw_text(self, screen):
        pass

lvs = [Test, Lv1, Lv2, Lv3]