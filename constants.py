import pygame
pygame.init()

class Consts:
    HEIGHT = 720
    WIDTH = 1280
    PLAYERSPEED = 5
    GRAVITY = 0.8
    PLAYER_H = 60
    PLAYER_W = 30
    JUMP_STR = 15
    MAX_ARROW_SPEED = 100
    ARROW_H = 15
    ARROW_W = 15
    ARROW_SPRITE_W = 150
    ARROW_SPRITE_H = 20
    COLLISION_LOSS = 15
    MIN_COLLISION_SPEED = 5
    FLAG_W = 60
    FLAG_H = 140
pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))

class Images:
    PLAYER_RIGHT = []
    PLAYER_LEFT = []
    for i in range(4):
        right = pygame.image.load(f'assets/images/player/right{i}.png').convert_alpha()
        left = pygame.image.load(f'assets/images/player/left{i}.png').convert_alpha()
        right = pygame.transform.scale(right, (Consts.PLAYER_W, Consts.PLAYER_H))
        left = pygame.transform.scale(left, (Consts.PLAYER_W, Consts.PLAYER_H))
        PLAYER_RIGHT.append(right)
        PLAYER_LEFT.append(left)
    STARTBUTTON = pygame.image.load('assets/images/start.png').convert_alpha()
    STARTBUTTON = pygame.transform.scale(STARTBUTTON, (210, 100))
    EXITBUTTON = pygame.image.load('assets/images/exit.png').convert_alpha()
    EXITBUTTON = pygame.transform.scale(EXITBUTTON, (220, 100))
    LOGO = pygame.image.load('assets/images/title.png').convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (650, 210))
    BACKGROUND = pygame.image.load('assets/images/background.png').convert_alpha()
    BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))
    FLAG = pygame.image.load('assets/images/flag.png').convert_alpha()
    FLAG = pygame.transform.scale(FLAG, (Consts.FLAG_W, Consts.FLAG_H))
    ARROW = pygame.image.load('assets/images/arrow.png').convert_alpha()
    ARROW = pygame.transform.scale(ARROW, (Consts.ARROW_SPRITE_W, Consts.ARROW_SPRITE_H))