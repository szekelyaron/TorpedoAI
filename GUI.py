import pygame
pygame.init()
pygame.display.set_caption("TorpedoAI")

WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
GREY = (40,50,200)


animating = True
pausing = False
while animating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                animating = False

            if event.type == pygame.K_SPACE:
                pausing = not pausing
    
    if not pausing:
        SCREEN.fill(GREY)
        pygame.display.flip()