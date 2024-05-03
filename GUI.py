import pygame
pygame.init()


pygame.display.set_caption("TorpedoAI")


animating = True
while animating:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: