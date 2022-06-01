import pygame
print("="*19, "DESAFIO 21", "="*19)
print("="*50)
print("Tocando Queen........")

pygame.mixer.init()
pygame.mixer.music.load("Super Mario Bros.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

print("="*50)
