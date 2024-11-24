import pygame
import sys
import random

pygame.init()

# These set us up to be able to use text and timers later
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asylum: Race')

font = pygame.font.SysFont('Arial', 30)
text = font.render("Welcome to Level 2: Race", True, (255, 255, 255))
start_time = pygame.time.get_ticks()

positionX, positionY = 0, 800
velocity = 5

brain = pygame.image.load(f"brain1-1.png.png")
brain_rect = brain.get_rect()
brain_rect.x = 0
brain_rect.y = 800

DARK_GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('Arial', 50)

def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x, y))

DISPLAY_DURATION = 3000
start_time = pygame.time.get_ticks()

def game_loop():
    running = True
    while running:
        elapsed_time = pygame.time.get_ticks() - start_time
        screen.fill((255,255,255))
        screen.fill(DARK_GREEN)
        screen.blit(brain, brain_rect)

        if elapsed_time <= DISPLAY_DURATION:
            draw_text("Welcome to the second Level: Race.", font, BLACK, 320, 350)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= velocity
        if keys[pygame.K_d]:
            x += velocity
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()
game_loop()


#Race game where if you try moving forward, the screen loops over and over again
#Only solved when moved left on first try