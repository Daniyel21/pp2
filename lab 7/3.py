import pygame

clock =pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame itProger Game")



player_speed = 20
player_x = 50
player_y = 450




limit_left, limit_right,limit_up, limit_down = 30, 560,30, 570
last_direction = 'down'
running = True
while running:
    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0),(player_x,player_y),25,0)
    
    if keys[pygame.K_LEFT] and player_x >limit_left:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x<limit_right:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y>limit_up:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y<limit_down:
        player_y += player_speed
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(50)
        