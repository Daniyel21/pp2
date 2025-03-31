import pygame

clock =pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame itProger Game")
icon = pygame.image.load('sprite/left_stay.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.transform.scale(pygame.image.load('sprite/pixilart-drawing.png'),(600, 600)).convert_alpha()

fire = pygame.transform.scale(pygame.image.load('sprite/campfire.png'),(100, 100)).convert_alpha()
door = pygame.transform.scale(pygame.image.load('sprite/campfire.png'),(50,200 )).convert_alpha()


myfont = pygame.font.Font('text/pheivrit.ttf', 40)

player_speed = 20
player_x = 50
player_y = 450


walk_left = [
    pygame.transform.scale(pygame.image.load('sprite/left_stay.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/left_go.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/left_stay.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/left_go1.png'),(80, 100)).convert_alpha()
]
walk_right = [
    pygame.transform.scale(pygame.image.load('sprite/right_stay.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/right_go.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/right_stay.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/right_go1.png'),(80, 100)).convert_alpha()
]
walk_up = [
    pygame.transform.scale(pygame.image.load('sprite/go_down1.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_down2.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_down1.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_down3.png'),(80, 100)).convert_alpha()
]
walk_down = [
    pygame.transform.scale(pygame.image.load('sprite/go_up1.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_up2.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_up1.png'),(80, 100)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('sprite/go_up3.png'),(80, 100)).convert_alpha()
]

player_anim_count = 0



limit_left, limit_right,limit_up, limit_down = 0, 530,300, 550
last_direction = 'down'
running = True
while running:
    screen.blit(bg, (0, 0))
    screen.blit(fire, (500,400))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    fire_rect = fire.get_rect(topleft=(500, 400))
    maindoorToleBie = door.get_rect(topleft=(250,130))

    if player_rect.colliderect(fire_rect):
        print("you lose")
        running = False
    
    if player_rect.colliderect(maindoorToleBie):
        bg = pygame.transform.scale(pygame.image.load('sprite/1floortolebie.png'),(600, 600)).convert_alpha()
        fire = pygame.transform.scale(pygame.image.load('sprite/campfire.png'),(0, 0)).convert_alpha()
        limit_up = -50
        limit_left = -50
        limit_right = 570
        

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        last_direction = 'left'
    elif keys[pygame.K_RIGHT]:
        last_direction = 'right'
    elif keys[pygame.K_UP]:
        last_direction = 'up'
    elif keys[pygame.K_DOWN]:
        last_direction = 'down'

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_RIGHT]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_UP]:
        screen.blit(walk_up[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_DOWN]:
        screen.blit(walk_down[player_anim_count], (player_x, player_y))
    else:
    
        if last_direction == 'left':
            screen.blit(pygame.transform.scale(pygame.image.load('sprite/left_stay.png'), (80, 100)).convert_alpha(), (player_x, player_y))
        elif last_direction == 'right':
            screen.blit(pygame.transform.scale(pygame.image.load('sprite/right_stay.png'), (80, 100)).convert_alpha(), (player_x, player_y))
        elif last_direction == 'up':
            screen.blit(pygame.transform.scale(pygame.image.load('sprite/go_down1.png'), (80, 100)).convert_alpha(), (player_x, player_y))
        elif last_direction == 'down':
            screen.blit(pygame.transform.scale(pygame.image.load('sprite/go_up3.png'), (80, 100)).convert_alpha(), (player_x, player_y))


    if keys[pygame.K_LEFT] and player_x >limit_left:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x<limit_right:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y>limit_up:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y<limit_down:
        player_y += player_speed
    


    if player_anim_count == 3:
        player_anim_count =0
    else:
        player_anim_count+=1
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(7)
        