import pygame
from player import Player
from terrain import Ground
from constants import Consts

running = True

WIDTH = 1280 
HEIGHT = 720 
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
terrains = []
terrains.append(Ground(0, 700, 1280, 20, "floor"))
terrains.append(Ground(0, 0, 20, 720, "left wall"))
terrains.append(Ground(1260, 0, 20, 720, "right wall"))
terrains.append(Ground(400, 600, 200, 20, "platform"))
terrains.append(Ground(300, 400, 200, 20, "platform"))
while running:
    clock.tick(60) 
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    

    player.handle_inputs(keys, events)
    for ground in terrains:
        print(f"{ground.tag}, Bottom: {player.terrain_collision_bottom(ground)}, Top: {player.terrain_collision_top(ground)}, Left: {player.terrain_collision_left(ground)}, Right: {player.terrain_collision_right(ground)}")
        player.terrain_collision(ground)
        ground.draw(screen)
    print(player.x_vel, player.y_vel)
    player.handle_movement()
    player.draw(screen)    
    
    pygame.display.flip()

pygame.quit()