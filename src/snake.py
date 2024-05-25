import pygame
from pygame.math import Vector2
from sys import exit 
import os, random

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183,111,122), block_rect)


class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x*cell_size), int(self.position.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)

pygame.init()
cell_size =40
cell_number= 20
image_path = os.path.join('assets', 'snake.png')
snake_icon = pygame.image.load(image_path)
pygame.display.set_icon(snake_icon)
screen =  pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)

