import pygame
from terrain import Ground

class Lv1:
    terrain = [Ground(0, 590, 320, 130),
               Ground(320, 460, 320, 260),
               Ground(640, 330, 320, 390),
               Ground(960, 200, 320, 520)]
    spawn = (20, 500)
