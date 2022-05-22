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
    BUTTON_L = 150
    BUTTON_W = 50
    BUTTON_W_PRESSED = 20
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
    GAME_BACKGROUND = pygame.image.load('assets/images/inGameBackground.png').convert_alpha()
    GAME_BACKGROUND = pygame.transform.scale(GAME_BACKGROUND, (Consts.WIDTH, Consts.HEIGHT))
    ARROW = pygame.image.load('assets/images/arrow.png').convert_alpha()
    ARROW = pygame.transform.scale(ARROW, (Consts.ARROW_SPRITE_W, Consts.ARROW_SPRITE_H))
    FLOOR = pygame.image.load('assets/images/floorTexture.png').convert_alpha()
    FLOOR = pygame.transform.scale(FLOOR, (Consts.WIDTH, Consts.HEIGHT))
    INTRO_TRANSITION = pygame.image.load('assets/images/introTransition.png').convert_alpha()
    INTRO_TRANSITION = pygame.transform.scale(INTRO_TRANSITION, (Consts.WIDTH, Consts.HEIGHT))
    DOOR = pygame.image.load('assets/images/door.png').convert_alpha()

class Sfx:
    FIRING = pygame.mixer.Sound("assets/sounds/firing.mp3")
    STUCK = pygame.mixer.Sound("assets/sounds/stuck.mp3")
    BUTTON = pygame.mixer.Sound("assets/sounds/button.mp3")
    VICTORY = pygame.mixer.Sound("assets/sounds/victory.mp3")
    TELEPORT = pygame.mixer.Sound("assets/sounds/teleport.mp3")

class Fonts:
    TXT_FONT = pygame.font.Font("assets/fonts/macondo.ttf", 32)