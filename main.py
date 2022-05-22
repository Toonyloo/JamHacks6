import pygame
from player import Player
from terrain import Ground
from arrow import Arrow
from constants import Consts, Images, Sfx, Fonts
from levels import lvs

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
pygame.display.set_caption('The Accursed Arrow') 
clock = pygame.time.Clock()  

running = True
game_state = 0
level = 0

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
                game_state = 3
        if 528 < mouse_pos[0] < 748 and 530 < mouse_pos[1] < 630:
            rect = pygame.Rect(535, 529, 215, 95)
            pygame.draw.rect(screen, (128, 128, 128), rect, 5)
            if mouse_buttons[0]:
                pygame.quit()
                break

    elif game_state == 1:
        screen.blit(Images.GAME_BACKGROUND, (0, 0))
        if mouse_buttons[0] and arrow.attached:
            arrow.shoot(mouse_pos)
        player.handle_inputs(keys, events)
        for ground in lvs[level].terrain:
            player.terrain_collision(ground)
            arrow.terrain_collision(ground)
            ground.draw(screen)
        
        for button in lvs[level].buttons:
            if pygame.sprite.collide_rect(arrow, button) or pygame.sprite.collide_rect(player, button):
                button.press()
            button.draw(screen)
        lvs[level].goal.draw(screen)

        for door in lvs[level].doors:
            if door.closed:
                player.terrain_collision(door)
                arrow.terrain_collision(door)
                door.draw(screen)
        
        lvs[level].draw_text(screen)

        
        if pygame.sprite.collide_mask(player, lvs[level].goal):
            Sfx.VICTORY.play()
            level += 1
            if level == len(lvs):
                game_state = 2
            else:
                player = Player(lvs[level].spawn)
                arrow = Arrow(player)
        
        player.handle_movement()
        arrow.handle_movement()
        arrow.attach()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and not arrow.attached:
                    arrow.swap()
        
        player.draw(screen) 
        arrow.draw(screen)
    elif game_state == 2:
        pass
    elif game_state == 3:
        if keys[pygame.K_SPACE]:
            game_state = 1
            level = 1
            player = Player(lvs[level].spawn)
            arrow = Arrow(player)
    pygame.display.flip()

pygame.quit()