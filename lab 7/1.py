import pygame
from datetime import date,timedelta,datetime
import math
WIDTH, HEIGHT = 800, 600
clock1 =pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame itProger Game")


center_x, center_y = WIDTH // 2, HEIGHT // 2

leftarm = pygame.transform.scale(pygame.image.load('lab7/leftarm.png'),(70, 700)).convert_alpha()
rightarm = pygame.transform.scale(pygame.image.load('lab7/rightarm.png'),(800, 1000)).convert_alpha()
bg = pygame.transform.scale(pygame.image.load('lab7/clock.png'),(WIDTH, HEIGHT)).convert_alpha()


running = True
while running:
    screen.blit(bg,(0,0))

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    angle_minutes = -(minutes * 6)
    angle_seconds = -(seconds * 6)

    leftarm_rotated = pygame.transform.rotate(leftarm, angle_seconds)
    leftarm_rect = leftarm_rotated.get_rect(center=(center_x, center_y))
    screen.blit(leftarm_rotated, leftarm_rect.topleft)

    rightarm_rotated = pygame.transform.rotate(rightarm, angle_minutes)
    rightarm_rect = rightarm_rotated.get_rect(center=(center_x, center_y))
    screen.blit(rightarm_rotated, rightarm_rect.topleft)

    pygame.display.update()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock1.tick(50)

