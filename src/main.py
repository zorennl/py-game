import pygame

screen = pygame.display.set_mode((1000, 800))
pygame.display.flip()

pygame.display.set_caption("First Game")

running = True

while running:
    for event in pygame.event.get(): 
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        if event.key == pygame.K_q:
            running = False
