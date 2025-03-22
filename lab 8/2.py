import pygame
import random
import sys
 
pygame.init()
pygame.mixer.init()
 
# pygame.mixer.music.load('music/scatman.mp3')
# pygame.mixer.music.play(-1)
 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
 
#Game Font
font = pygame.font.Font(None,30)
 
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
COLOR = (0,0,0)
 
# Snake Settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15
 
# Food settings
food_list = [[random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10] for _ in range(4)]
def spawn_food():
    while True:
        new_food = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        if new_food not in snake_body:
            return new_food
food_spawn = True
 
game_score = 0
 
isRunning = True
dot =0
 
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()  # Fixed sys.quit() to sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"    
 
 
 
    # Move snake based on direction
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10
 
 
    # Insert new position
    snake_body.insert(0, list(snake_pos))  
   
    # Check if food is eaten
    if snake_pos in food_list:
        game_score += 1
        food_list.remove(snake_pos)
        food_list.append(spawn_food())
    else:
        snake_body.pop()
 
    if not food_spawn:
        food_list = [[random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10] for _ in range(4)]
    food_spawn = True

    if game_score %4 == 0 and game_score !=0:
        if dot ==1:
            COLOR =(random.randint(0, 200), random.randint(0, 200), random.randint(0, 255))
            dot = 0
            speed+=5
    else:
        dot=1

    screen.fill(COLOR)
 
    # Check for collision with walls
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False
 
    # Check for collision with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False
   
   
    # Update screen
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    for food in food_list:
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))
 
    game_score_text = font.render(f"Your score: {game_score}",True,'white')
    screen.blit(game_score_text,(20,20))
    game_level_text = font.render(f"Level: {int(game_score/4)}",True,'white')
    screen.blit(game_level_text,(450,20))
    pygame.display.update()
 
    pygame.display.flip()
    clock.tick(speed)
   
 
 
game_over_text = font.render("GAME OVER", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text,game_over_rectangle)
pygame.display.update()
pygame.time.wait(600)
pygame.mixer