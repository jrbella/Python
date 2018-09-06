    # -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:04:59 2018
@author: Kwill
"""

#TODO: clean up code
#TODO: make it modular
#TODO: add class method for direction and speed updata
#TODO: convert to singleton/static class
#TODO: remove hard coding
#TODO: add constraint for self-intersection
#TODO: Overlays and text
#TODO: random white box on food spawn??
import pygame
import random

display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakey McSnakeface')
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()

class Snake:
    
    def __init__(self,display_width,display_height):
        self.display_width = display_width
        self.display_height = display_height
    
    def random_start(self):
        self.size = 1
        self.body = []
        self.speed = [0,0] # left or up
        self.speed[random.sample([0,1],1)[0]] = 10
        
        x = random.sample(range(self.display_width),1)[0]
        y = random.sample(range(self.display_height),1)[0]
        self.body.append((x,y))
        self.tail = [x,y]
        if self.speed[0] !=0:
            self.dir_y = 0
            self.dir_x = random.sample([-1,1],1)[0]
        else:
            self.dir_x = 0
            self.dir_y = random.sample([-1,1],1)[0]
    
        return x,y

    def move_forward(self,x,y):
        self.body.pop(0)
        self.body.append((x,y))
        
    def draw_snake(self,x,y):
        self.move_forward(x,y)
        for piece in self.body:
            pygame.draw.rect(gameDisplay,white,(piece[0],piece[1],10,10))
   
    def grow(self):
        self.size +=1
        x_new = self.tail[0] - self.dir_x*10
        y_new = self.tail[1] - self.dir_y*10
        self.tail = [self.body[0][0],self.body[0][1]]
        self.body.append((x_new,y_new))
    
    def update_vector(self,dir_x,dir_y,speed):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed = speed
        
class Food:
    
    def __init__(self,display_width,display_height):
        self.spawn_width = display_width - 2*10
        self.spawn_height = display_height - 2*10

    def spawn(self):
        x = random.sample(range(self.spawn_width),1)[0]
        y = random.sample(range(self.spawn_height),1)[0]
        return x,y
# NOTE: coordinates are set as quadrant 1
    



def game_loop(display_width,display_height):
    snake = Snake(display_width,display_height)
    food = Food(display_width,display_height)
    exiting = False
    gameDisplay.fill(black)
    x,y = snake.random_start()
    x_food,y_food = food.spawn()
    
    while not exiting:
        x = x+snake.dir_x*snake.speed[0]
        y = y+snake.dir_y*snake.speed[1]
        gameDisplay.fill(black)
        snake.draw_snake(x,y)
        pygame.draw.rect(gameDisplay,(255,0,0),(x_food,y_food,10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exiting = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.update_vector(-1,0,[10,0])
                if event.key == pygame.K_RIGHT:
                    snake.update_vector(1,0,[10,0])
                if event.key == pygame.K_UP:
                    snake.update_vector(0,-1,[0,10])
                if event.key == pygame.K_DOWN:
                    snake.update_vector(0,1,[0,10])
        if x+10 >= display_width or x <= 0 or y <=0 or y >=display_height-10:
            x,y = snake.random_start()
            
        if pygame.Rect((x,y),(10,10)).colliderect(pygame.Rect((x_food,y_food),(10,10))):
            snake.grow()
            x_food,y_food = food.spawn()
        
        pygame.display.update()
        clock.tick(10)
        
game_loop(display_width,display_height)
pygame.quit()