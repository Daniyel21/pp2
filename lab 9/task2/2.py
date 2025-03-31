import pygame
import random
import time

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Snake color
RED = (255, 0, 0)  # Food (1 point)
BLUE = (135, 206, 235)  # Food (2 points)
GOLD = (255, 215, 0)  # Food (3 points)
BLACK = (0, 0, 0)  # Background color
COLOR = (0,0,0)

# Dictionary mapping food weights to colors
food_colors = {1: RED, 2: BLUE, 3: GOLD}

# Snake settings
snake_pos = [100, 50]  # Initial position
snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body
snake_direction = "RIGHT"  # Initial direction
change_to = snake_direction  # Direction change buffer
speed = 10  # Snake speed
game_score = 0  # Score counter
isRunning = True
dot = 0  # Helper variable for level progression

food_list = []  # Stores food positions and their weights


def spawn_food():
    """Generates a new food item at a random position with a random weight."""
    while True:
        x = random.randrange(0, WIDTH // 10) * 10
        y = random.randrange(0, HEIGHT // 10) * 10
        weight = random.choice([1, 2, 3])  # Random weight
        new_food = [x, y, weight]  # Position + weight

        if new_food[:2] not in [food[:2] for food in food_list] and new_food[:2] not in snake_body:
            return new_food


def update_food():
    """Ensures there are always 4 food items on the screen."""
    while len(food_list) < 4:
        food_list.append(spawn_food())


# Create initial food items
for _ in range(4):
    food_list.append(spawn_food())

# Main game loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False  # Exit game
        elif event.type == pygame.KEYDOWN:  # Detect key presses
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Move the snake based on the current direction
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Insert the new position at the head of the snake
    snake_body.insert(0, list(snake_pos))

    # Check if the snake eats food
    for food in food_list[:]:  # Iterate over a copy of the food list
        if snake_pos[:2] == food[:2]:  # Check if snake's head touches food
            game_score += food[2]  # Increase score based on food weight
            food_list.remove(food)  # Remove eaten food
            break
    else:
        snake_body.pop()  # Remove the tail if no food is eaten

    update_food()  # Ensure there are always 4 food items

    # Level progression: increase speed every 4 points
    if game_score % 4 == 0 and game_score != 0:
        if dot == 1:
            COLOR =(random.randint(0, 200), random.randint(0, 200), random.randint(0, 255))
            dot = 0
            speed+=5
    else:
        dot = 1

    screen.fill(COLOR) # Clear the screen

    # Check for wall collisions
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False  # Game over

    # Check for self-collision
    if snake_pos in snake_body[1:]:
        isRunning = False  # Game over

    # Draw the snake
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))

    # Draw the food
    for food in food_list:
        pygame.draw.rect(screen, food_colors[food[2]], pygame.Rect(food[0], food[1], 10, 10))

    # Display the score and level
    game_score_text = font.render(f"Score: {game_score}", True, WHITE)
    screen.blit(game_score_text, (20, 20))
    game_level_text = font.render(f"Level: {game_score // 4}", True, WHITE)
    screen.blit(game_level_text, (450, 20))

    pygame.display.update()
    clock.tick(speed)  # Control game speed

# Game over screen
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
