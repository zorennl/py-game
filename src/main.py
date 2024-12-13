import pygame

screen = pygame.display.set_mode((1000, 800))
pygame.display.flip()

pygame.display.set_caption("First Game")

rect = pygame.Rect(10, 20, 30, 30)
surface = pygame.image.load('/home/zmynz/vss/python/first-game/assets/textures/player.png')

running = True
while running:
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
