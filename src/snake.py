import pygame
from pygame.math import Vector2
from sys import exit 
import os, random

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        s1_path = os.path.join('assets', 'head_up.png')
        self.head_up = pygame.image.load(s1_path).convert_alpha()
        s2_path = os.path.join('assets', 'head_down.png')
        self.head_down = pygame.image.load(s2_path).convert_alpha()
        s3_path = os.path.join('assets', 'head_right.png')
        self.head_right = pygame.image.load(s3_path).convert_alpha()
        s4_path = os.path.join('assets', 'head_left.png')
        self.head_left = pygame.image.load(s4_path).convert_alpha()
        s5_path = os.path.join('assets', 'tail_up.png')
        self.tail_up = pygame.image.load(s5_path).convert_alpha()
        s6_path = os.path.join('assets', 'tail_down.png')
        self.tail_down = pygame.image.load(s6_path).convert_alpha()
        s7_path = os.path.join('assets', 'tail_right.png')
        self.tail_right = pygame.image.load(s7_path).convert_alpha()
        s8_path = os.path.join('assets', 'tail_left.png')
        self.tail_left = pygame.image.load(s8_path).convert_alpha()
        s9_path = os.path.join('assets', 'body_vertical.png')
        self.body_vertical = pygame.image.load(s9_path).convert_alpha()
        s10_path = os.path.join('assets', 'body_horizontal.png')
        self.body_horizontal = pygame.image.load(s10_path).convert_alpha()
        s11_path = os.path.join('assets', 'body_topright.png')
        self.body_tr = pygame.image.load(s11_path).convert_alpha()
        s12_path = os.path.join('assets', 'body_topleft.png')
        self.body_tl = pygame.image.load(s12_path).convert_alpha()
        s13_path = os.path.join('assets', 'body_bottomright.png')
        self.body_br = pygame.image.load(s13_path).convert_alpha()
        s14_path = os.path.join('assets', 'body_bottomleft.png')
        self.body_bl = pygame.image.load(s14_path).convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()


        for index,block in enumerate(self.body):
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                prevoius_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if prevoius_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif prevoius_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if prevoius_block.x == -1 and next_block.y == -1 or prevoius_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif prevoius_block.x == -1 and next_block.y == 1 or prevoius_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif prevoius_block.x == 1 and next_block.y == -1 or prevoius_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif prevoius_block.x == 1 and next_block.y == 1 or prevoius_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x*cell_size), int(self.position.y*cell_size), cell_size, cell_size)
        screen.blit(fruit, fruit_rect)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grid()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit = Fruit()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        exit()
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        fruit_rect = fruit.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(fruit_rect.left, fruit_rect.top, fruit_rect.width + score_rect.width + 6, fruit_rect.height)
        pygame.draw.rect(screen, (167,209,61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(fruit, fruit_rect)
    
    def draw_grid(self):
        for x in range(cell_number):
            if x % 2 == 0:
                for y in range(cell_number):
                    if y % 2 == 0:
                        cell_rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, (167,209,61), cell_rect)
            else:
                for y in range(cell_number):
                    if y % 2 != 0:
                        cell_rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, (167,209,61), cell_rect)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size =40
cell_number= 20
snake_path = os.path.join('assets', 'snake.png')
snake_icon = pygame.image.load(snake_path)
fruit_path = os.path.join('assets', 'fruit.png')
fruit_icon = pygame.image.load(fruit_path)
fruit = pygame.transform.scale(fruit_icon, (cell_size, cell_size))
pygame.display.set_icon(snake_icon)
screen =  pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 25)


screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)
main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == screen_update:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

