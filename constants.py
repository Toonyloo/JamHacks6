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
    ARROW_H = 10
    ARROW_W = 10
    COLLISION_LOSS = 25
pygame.display.set_mode((Consts.WIDTH, Consts.HEIGHT))

class Images:
    PLAYER = pygame.image.load("assets/images/placeholder.png").convert_alpha()
    PLAYER = pygame.transform.scale(PLAYER, (Consts.PLAYER_W, Consts.PLAYER_H))
    STARTBUTTON = pygame.image.load('assets/images/start.png')
    STARTBUTTON = pygame.transform.scale(STARTBUTTON, (210, 100))
    EXITBUTTON = pygame.image.load('assets/images/exit.png')
    EXITBUTTON = pygame.transform.scale(EXITBUTTON, (220, 100))
    LOGO = pygame.image.load('assets/images/title.png')
    LOGO = pygame.transform.scale(LOGO, (650, 210))
    BACKGROUND = pygame.image.load('assets/images/background.png')
    BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))