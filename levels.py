import pygame
from terrain import Ground, Goal

class Test:
    terrain = [Ground(0, 700, 1280, 20, "floor"),
Ground(0, 0, 20, 720, "left wall"),
Ground(1260, 0, 20, 720, "right wall"),
Ground(400, 600, 200, 20, "platform"),
Ground(300, 400, 200, 20, "platform"),
Ground(0, 0, 1280, 20, "ceiling")]

class Lv1:
    terrain = [Ground(0, 590, 320, 130),
               Ground(320, 460, 320, 260),
               Ground(640, 330, 320, 390),
               Ground(960, 200, 320, 520), 
               Ground(0, 0, 20, 720, "left wall"),
               Ground(1260, 0, 20, 720, "right wall"),
               Ground(0, 0, 1280, 20, "ceiling")]
    spawn = (20, 500)
    goal = Goal(1120, 200)

class Lv2:
    terrain = [Ground(0, 700, 1280, 20, "floor"),
Ground(0, 0, 20, 720, "left wall"),
Ground(1260, 0, 20, 720, "right wall"),
Ground(0, 0, 1280, 20, "ceiling"),
Ground(400, 600, 200, 20, "platform"),
Ground(300, 400, 200, 20, "platform")]
    spawn = (20, 500)
    goal = Goal(1120, 200)

class Lv3:
    pass

lvs = [Test, Lv1, Lv2, Lv3]