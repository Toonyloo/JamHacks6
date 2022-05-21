import pygame
from player import Player
from terrain import Ground
from constants import Consts

running = True

WIDTH = 1280 # TODO
HEIGHT = 720 # TODO
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')  # TODO
clock = pygame.time.Clock()  

running = True

def draw_title_screen():
    screen.fill(WHITE)
    #TODO

player = Player()
ground = Ground(0, 700, 1280, 20)
while running:
    clock.tick(FPS) 
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    
    if pygame.sprite.collide_rect(player, ground):
        player.grounded = True
        player.y = ground.y - Consts.PLAYER_H
    
    player.handle_inputs(keys, events)
    player.handle_movement()
    player.draw(screen)
    ground.draw(screen)
    
    print(player.y_vel, player.grounded)
    pygame.display.flip()

pygame.quit()