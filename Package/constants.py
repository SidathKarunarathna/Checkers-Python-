import pygame

WIDTH,HEIGHT=800,800
ROWS,COLS=8,8
SQUARE_SIZE=WIDTH//COLS

RED = (255,178,102)
WHITE=(255,255,255)
BLACK = (102,51,0)
BLUE=(0,0,255)
GREY=(128,128,128)
DARK=(0,0,0)
GREEN =(0,255,0)
BACKGROUND =(243,211,116)

CROWN =pygame.transform.scale(pygame.image.load('assets/crown.png'),(44,25))
LOGO = pygame.transform.scale(pygame.image.load('assets/logo.png'),(270,270))