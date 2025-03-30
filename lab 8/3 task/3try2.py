import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (140,140,140)
DARK_GRAY = (100,100,100)

runing = True
drawing = False

buttons = [
    {"rect": pygame.Rect(2, 2, 21, 21), "image": pygame.transform.scale(pygame.image.load("lab 8/3 task/paint-brush_13329107.png"), (21, 21))},
    {"rect": pygame.Rect(2, 27, 21, 21), "image": pygame.transform.scale(pygame.image.load("lab 8/3 task/eraser_9363850.png"), (21, 21))},
    {"rect": pygame.Rect(2, 52, 21, 21), "image": pygame.transform.scale(pygame.image.load("lab 8/3 task/vecteezy_colored-grunge-circle-brush-ink-frame_21975741.png"), (21, 21))},
    {"rect": pygame.Rect(2, 77, 21, 21), "image": pygame.transform.scale(pygame.image.load("lab 8/3 task/vecteezy_black-rectangle-isolated_42730310.png"), (18, 18))},
    {"rect": pygame.Rect(2, 102, 21, 21), "image": pygame.transform.scale(pygame.image.load("lab 8/3 task/color-illustrator_401085.png"), (21, 21))}
]
active_index = None
active_index_for0 = None
active_index_for1 = None



rect = pygame.Rect(0, 0, 25, 125)

buttonsfor4 = [
    {"rect": pygame.Rect(27, 102, 150, 75), "color": GRAY},
    {"rect": pygame.Rect(30, 109, 100, 16), "color": RED},
    {"rect": pygame.Rect(30, 132, 100, 16), "color": GREEN},
    {"rect": pygame.Rect(30, 155, 100, 16), "color": BLUE}
]
red,green,blue = 0,0,0

buttonsfor0 = [
    {"spawn": (35,26), "radius": 5},
    {"spawn": (55,26), "radius": 10},
    {"spawn": (85,26), "radius": 15},
    {"spawn": (125,26), "radius": 20}
]
rad = 5

buttonsfor1 = [
    {"spawn": (40,49), "radius": 10},
    {"spawn": (70,49), "radius": 15},
    {"spawn": (110,49), "radius": 20}
]
buttonfor1 = pygame.Rect(132, 27, 43, 48)
font = pygame.font.SysFont("Verdana", 20)
buttfor1 = font.render("ALL", True, BLACK)
rad1 = 10

q = False
rects = []

screen.fill((WHITE))
while runing:
    pygame.draw.rect(screen,(200,200,200),(0,0,177,177))

    pygame.draw.rect(screen, (200,200,200), rect)

  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if active_index == 0:
                if event.pos[0] >177 or event.pos[1]>177:
                    drawing = True
                    last_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                if event.type == pygame.MOUSEMOTION and drawing:
                    if last_pos:
                        pygame.draw.line(screen,(red*2.55,green*2.55,blue*2.55), last_pos, event.pos, rad)
                    last_pos = event.pos

            if active_index == 0:
                mouse_x, mouse_y = event.pos
                for index,i in enumerate(buttonsfor0):
                    if (mouse_x - i["spawn"][0])**2 + (mouse_y - i["spawn"][1])**2 <= i["radius"] **2:
                        active_index_for0 = index

            if active_index == 1:
                if event.pos[0] >177 or event.pos[1]>177:
                    drawing = True
                    last_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                if event.type == pygame.MOUSEMOTION and drawing:
                    if last_pos:
                        pygame.draw.line(screen, WHITE, last_pos, event.pos, rad1)
                    last_pos = event.pos

            if active_index == 1:
                mouse_x, mouse_y = event.pos
                for index,i in enumerate(buttonsfor1):
                    if buttonfor1.collidepoint(event.pos):
                        active_index_for1 = 3
                        break
                    if (mouse_x - i["spawn"][0])**2 + (mouse_y - i["spawn"][1])**2 <= i["radius"] **2:
                        active_index_for1 = index        



            if active_index == 4:
                mouse_x, mouse_y = event.pos
                if 109 <= mouse_y <= 125:  
                    red = max(0, min(100, mouse_x - 30))
                elif 132 <= mouse_y <= 148: 
                    green = max(0, min(100, mouse_x -30))
                elif 155 <= mouse_y <= 172: 
                    blue = max(0, min(100, mouse_x - 30))

            for index, button in enumerate(buttons):
                if button["rect"].collidepoint(event.pos):
                    active_index = index
                    break
                
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if active_index == 3:
            if pygame.MOUSEBUTTONDOWN == event.type:
                if event.button == 1:  # Левая кнопка мыши - начинаем рисование прямоугольника
                    spawn = event.pos  
                    temp_width = 0
                    temp_height = 0
                    q = False
                    rectangle_backup = screen.copy()  # Сохраняем фон перед рисованием прямоугольника
        
                elif event.button == 3:  # Уменьшаем размер прямоугольника
                    temp_width = max(5, temp_width - 5)  
                    temp_height = max(5, temp_height - 5)  
        
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                x, y = min(spawn[0], sec_pos[0]), min(spawn[1], sec_pos[1])
                temp_width, temp_height = abs(spawn[0] - sec_pos[0]), abs(spawn[1] - sec_pos[1])
        
                screen.blit(rectangle_backup, (0, 0))  # Восстанавливаем фон, убирая старый прямоугольник
                pygame.draw.rect(screen, (red * 2.55, green * 2.55, blue * 2.55), (x, y, temp_width, temp_height))
        
            if pygame.MOUSEBUTTONUP == event.type:
                q = True



        if active_index == 2:
            if pygame.MOUSEBUTTONDOWN == event.type:
                if event.button == 1:  # Левая кнопка мыши - начинаем рисование круга
                    spawn = event.pos  
                    temp_rad = 0  # Начальный радиус круга
                    q = False
                    circle_backup = screen.copy()  # Сохраняем фон перед рисованием круга
        
                elif event.button == 3:  # Правая кнопка мыши - уменьшаем радиус круга
                    temp_rad = max(5, temp_rad - 5)  # Уменьшаем радиус, но не даем уйти в 0
        
            if pygame.MOUSEMOTION == event.type and not q:
                    temp_rad = int(sqrt((event.pos[0] - spawn[0])**2 + (event.pos[1] - spawn[1])**2))
        
                    screen.blit(circle_backup, (0, 0))  # Восстанавливаем фон, убирая старый круг
                    pygame.draw.circle(screen, (red * 2.55, green * 2.55, blue * 2.55), spawn, temp_rad)
        
            if pygame.MOUSEBUTTONUP == event.type:
                    q = True

        
        if event.type == pygame.MOUSEMOTION and drawing:
            if active_index == 0:
                if last_pos:
                    pygame.draw.line(screen, (red * 2.55, green * 2.55, blue * 2.55), last_pos, event.pos, rad)
                    last_pos = event.pos
            if active_index ==1:
                if last_pos:
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, rad1)
                    last_pos = event.pos


    for index, button in enumerate(buttons):
        if active_index == index:
            color = DARK_GRAY
        else:
            color = GRAY
        pygame.draw.rect(screen, color, button["rect"])
        screen.blit(button["image"], button["rect"].topleft)

    if active_index == 0:
        pygame.draw.rect(screen,(GRAY),pygame.Rect(27, 2, 120, 48)) 
        for index,i in enumerate(buttonsfor0):
            pygame.draw.circle(screen,(red*2.55,green*2.55,blue*2.55), i["spawn"],i["radius"]) 
            if index == active_index_for0:
                rad = i["radius"]

    if active_index == 1:
        pygame.draw.rect(screen,(GRAY),pygame.Rect(27, 27, 150, 48))
        pygame.draw.rect(screen,(DARK_GRAY),buttonfor1)
        screen.blit(buttfor1, (137,35))
        for index,i in enumerate(buttonsfor1):
            pygame.draw.circle(screen,WHITE, i["spawn"],i["radius"])
            if active_index_for1 == 3:
                pygame.draw.rect(screen,WHITE,(177,0,463,480))
                pygame.draw.rect(screen,WHITE,(0,177,640,303))
            if index == active_index_for1:
                rad1 = i["radius"]
    active_index_for1 = None

    if active_index == 4:
        for button in buttonsfor4:
            pygame.draw.rect(screen, button["color"], button["rect"])
        pygame.draw.rect(screen,(red*2.55,green*2.55,blue*2.55),pygame.Rect(135, 108, 35, 63))
        
        pygame.draw.circle(screen, BLACK, (30 + red, 117), 8)  
        pygame.draw.circle(screen, BLACK, (30 + green, 140),8)  
        pygame.draw.circle(screen, BLACK, (30 + blue, 163), 8)
    

    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
