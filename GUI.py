from engine import Player

import pygame
pygame.init()
pygame.display.set_caption("TorpedoAI")

SQ_SIZE = 35
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE

WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
INDENT = 5

WHITE = (255,255,255)
GREY = (40,50,60)
RED = (255,40,0)
BLUE = (0,0,128)
GREEN = (50,200,150)

def draw_grid(left = 0, top = 0):
    for i in range(100) :
        x = left + i % 10 * SQ_SIZE 
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x,y, SQ_SIZE,SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE,square, width=3)

def draw_ships (player, left = 0, top = 0):
    for ship in player.ships:
        x = left + ship.col*SQ_SIZE+INDENT
        y = top + ship.row* SQ_SIZE+INDENT
        if ship.orientation == "h":
            width = ship.size * SQ_SIZE- 2 * INDENT
            height = SQ_SIZE-2 * INDENT
        else:
            width = SQ_SIZE - 2*INDENT
            height = ship.size * SQ_SIZE - 2* INDENT
        rectangle = pygame. Rect(x, y, width, height)
        pygame.draw.rect (SCREEN, GREEN, rectangle, border_radius = 15)

player1 = Player()
player2 = Player()

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

        draw_ships (player1, top = (HEIGHT-V_MARGIN) //2 + V_MARGIN)
        draw_ships(player2, left = (WIDTH-H_MARGIN)//2 + H_MARGIN)
        pygame.display.flip()