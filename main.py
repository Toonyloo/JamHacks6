import pygame
from player import Player
from terrain import Ground
from arrow import Arrow
from constants import Consts, Images
import levels

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
game_state = 0

def draw_title_screen():
    screen.fill((0, 140, 148))
    screen.blit(Images.STARTBUTTON, (535, 400))
    screen.blit(Images.EXITBUTTON, (528, 530))
    screen.blit(Images.LOGO, (315, 60))
    screen.blit(Images.BACKGROUND, (0, 0))


while running:
    clock.tick(60) 
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    
    if game_state == 0:
        draw_title_screen()
        if 535 < mouse_pos[0] < 745 and 400 < mouse_pos[1] < 500:
            rect = pygame.Rect(535, 400, 210, 94)
            pygame.draw.rect(screen, (128, 128, 128), rect, 5)
            if mouse_buttons[0]:
                game_state = 1
                player = Player(levels.Lv1.spawn)
                arrow = Arrow(player)
                terrains = levels.Lv1.terrain
        if 528 < mouse_pos[0] < 748 and 530 < mouse_pos[1] < 630:
            rect = pygame.Rect(535, 529, 215, 95)
            pygame.draw.rect(screen, (128, 128, 128), rect, 5)
            if mouse_buttons[0]:
                pygame.quit()
                break
    if game_state == 1:
        if keys[pygame.K_SPACE] and arrow.attached:
            arrow.shoot(mouse_pos)
        player.handle_inputs(keys, events)
        for ground in terrains:
            print(ground)
            # print(f"{ground.tag}, Bottom: {player.terrain_collision_bottom(ground)}, Top: {player.terrain_collision_top(ground)}, Left: {player.terrain_collision_left(ground)}, Right: {player.terrain_collision_right(ground)}")
            player.terrain_collision(ground)
            arrow.terrain_collision(ground)
            ground.draw(screen)
        player.handle_movement()
        arrow.handle_movement()
        
        player.draw(screen) 
        arrow.draw(screen)
        
    pygame.display.flip()

pygame.quit()