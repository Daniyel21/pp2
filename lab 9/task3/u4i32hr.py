import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

# Colors (0-100 scale converted to (0-255))
red, green, blue = 50, 80, 100

active_index = 3
point1, point2, point3 = None, None, None
q = False
triangle1_backup = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if active_index == 3:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                point1 = event.pos
                point2, point3 = None, None
                q = False
                triangle1_backup = screen.copy()  # Save background before drawing

            if event.type == pygame.MOUSEMOTION and not q:  # When dragging to draw
                sec_pos = event.pos
                base = abs(sec_pos[0] - point1[0])  # Base length
                mid_x = (point1[0] + sec_pos[0]) // 2  # Midpoint X for isosceles

                height = int((math.sqrt(3) / 2) * base)  # Compute height
                point2 = (sec_pos[0], point1[1])  # Second point at the same Y-level
                point3 = (mid_x, point1[1] - height)  # Third point above the base

                screen.blit(triangle1_backup, (0, 0))  # Restore background
                pygame.draw.polygon(screen, (int(red * 2.55), int(green * 2.55), int(blue * 2.55)), [point1, point2, point3], 0)

            if event.type == pygame.MOUSEBUTTONUP:  # When mouse is released
                q = True

    pygame.display.flip()

pygame.quit()
