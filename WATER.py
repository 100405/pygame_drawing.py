import pygame
import pickle
from os import path

clock = pygame.time.Clock()
fps = 40

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dogs adventure')

# load the images of the game
background_img = pygame.image.load("images1/download.jpg")
background_img = pygame.transform.scale(background_img, (800, 600))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (255,255,255), (0, line * tile_size),)

run = True
while run:
    screen.blit(background_img, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.update()
pygame.quit()