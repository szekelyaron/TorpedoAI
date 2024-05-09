import pygame
pygame.init()
pygame.display.set_caption("TorpedoAI")

SQ_SIZE = 35
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE

WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
GREY = (40,50,60)
RED = (255,40,0)
BLUE = (0,0,128)

def draw_grid(left = 0, top = 0):
    for i in range(100) :
        x = left + i % 10 * SQ_SIZE 
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x,y, SQ_SIZE,SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE,square, width=3)

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
        draw_grid()
        draw_grid(left = (WIDTH-H_MARGIN)//2 + H_MARGIN,top = (HEIGHT-V_MARGIN)//2 + V_MARGIN)

        draw_grid(top = (HEIGHT-V_MARGIN)//2 + V_MARGIN)
        draw_grid(left = (WIDTH-H_MARGIN)//2 + H_MARGIN)
        pygame.display.flip()