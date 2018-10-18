import pygame

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

while True:
    invoer = str(input("Voor invoer in: "))
    if invoer == 'stop':
        pygame.mixer.music.stop()
    if invoer == '+':
        volOud = pygame.mixer.music.get_volume()
        nieuweVol = volOud + 0.1
        if nieuweVol > 1:
            print('hij staat op zn hardst')
        else:
            pygame.mixer.music.set_volume(nieuweVol)
    if invoer == '-':
        volOud = pygame.mixer.music.get_volume()
        nieuweVol = volOud - 0.1
        if nieuweVol < 0:
            print('hij staat op zn zachtst')
        else:
            pygame.mixer.music.set_volume(nieuweVol)
    if invoer == 'pauze':
        pygame.mixer.music.pause()
    if invoer == 'start':
        pygame.mixer.music.unpause()