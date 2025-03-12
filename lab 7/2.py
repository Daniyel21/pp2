import pygame 

pygame.init()
clock1 = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame itProger Game")

bg = pygame.transform.scale(pygame.image.load('lab7/bgmusic.png'), (600, 600)).convert_alpha()

_songs = ['lab7/Blinding_Lights.mp3', 'lab7/Call_Out_My_Name.mp3', 'lab7/Cant_Feel_My_Face.mp3', 'lab7/Save_Your_Tears.mp3', 'lab7/The_Hills.mp3']
play = False

pygame.mixer.music.load(_songs[0])


def play_next_song():
    global _songs, play
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    play = True

running = True
while running:
    screen.blit(bg, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                _songs = _songs[-1:] + _songs[:-1]
                pygame.mixer.music.load(_songs[0])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                play_next_song()

            elif event.key == pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                    play = False
                else:
                    pygame.mixer.music.play()
                    play = True

    clock1.tick(50)
