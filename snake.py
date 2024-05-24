import pygame
import sys
from sys import exit 
import os

pygame.init()
image_path = os.path.join('assets', 'snake.png')
snake_icon = pygame.image.load(image_path)
pygame.display.set_icon(snake_icon)
screen =  pygame.display.set_mode((800,400))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)

            

