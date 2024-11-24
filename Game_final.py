import pygame
import sys
import random as rand
import turtle as trtl

from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asylum')

#GLOBAL VARIABLES
platform_width = 128
platform_height = 10

platform_img = pygame.image.load(f"platform-2.png")



user_input = ""

# Fonts
font = pygame.font.SysFont('Times New Roman', 30)

DISPLAY_DURATION = 3000  # 3 seconds
start_time = pygame.time.get_ticks()

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

#color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

characters = ""

run = True
while run:
    elapsed_time = pygame.time.get_ticks() - start_time
    screen.fill(WHITE)

    for detect in pygame.event.get():
        if detect.type == KEYDOWN:
            characters = detect.unicode
            if detect.key == K_RETURN:
                global text
                text = characters
                
    


    draw_text(characters, font, (0,0,0), 400, 400)

    if elapsed_time <= DISPLAY_DURATION:
        draw_text("Hello. Welcome to the first Level: Asylum", font, (0,0,0), 180, 350)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()