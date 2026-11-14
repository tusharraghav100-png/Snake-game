import pygame
import math   
import sys
import random as randit
import time


pygame.init()

width,height = 600,600
Sy = 300
Sx = 300
RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

direction = RIGHT
snake_body = [
      [300 , 300],
      [280 , 280],
      [260 , 260]
      ]

clock = pygame.time.Clock()
snake_head = snake_body[0]
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake game")

score = 0
font = pygame.font.Font()
snake = pygame.Surface((20,20))
snake_rect = snake.get_rect(center=(width//2, height//2))
snake.fill('light green')



#food
food = pygame.Surface((10,10))
food.fill('red')
food_rect = food.get_rect(
    center=(randit.randint(10,590), randit.randint(10,590))
)
#border 
border1 = pygame.Surface((600 , 10))
borderrect = border1.get_rect(midtop = ((width//2 , height-600)))
border2 = pygame.Surface((600 , 10))
borderrect2 = border2.get_rect(midbottom = ((width//2 , 600)))
border3 = pygame.Surface((10 , 600))
borderrect3 = border3.get_rect(midleft = ((0 , height//2)))
border4 = pygame.Surface((10 , 600))
borderrect4 = border4.get_rect(center = ((600 , height//2)))
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w :
               direction = UP
               
        if i.type == pygame.KEYDOWN:
           
            if i.key == pygame.K_s :
                   direction = DOWN
                
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a :
                direction = LEFT
               
        if i.type == pygame.KEYDOWN:
                    
                    if i.key == pygame.K_d :
                        direction = RIGHT
    dt = clock.tick(60) / 1000         
    if direction == UP:
        Sy -= 4
    elif direction == DOWN:
         Sy += 4
    elif direction == LEFT:
           Sx -= 4
    elif direction == RIGHT:
          Sx += 4
    new_head = [Sx , Sy]
    
    snake_body.insert(0, new_head)
    
    snake_rect.centery = Sy
    snake_rect.centerx = Sx
   

    label = font.render(f"score = {score}", True , "blue")
    screen.fill('cyan')
    screen.blit(label , (50,10))
   
    screen.blit(food , food_rect)
    if snake_rect.colliderect(food_rect):
         food_rect.center = (
        randit.randint(15,580),
        randit.randint(15,580) 
       
          
    )
         score += 1
    else:
          snake_body.pop()
    if snake_rect.colliderect(borderrect):
            
             time.sleep(2)
             running = False
    if snake_rect.colliderect(borderrect2):
             
             time.sleep(2)
             running = False
    if snake_rect.colliderect(borderrect3):
             
             time.sleep(2)
             running = False
    if snake_rect.colliderect(borderrect4):
                
                 time.sleep(2)
                 running = False
    for i in snake_body:
          screen.blit(snake , (i[0], i[1]))
    screen.blit(border4, borderrect4)
    screen.blit(border3,borderrect3)
    screen.blit(border2,borderrect2)
    screen.blit(border1,borderrect)
    
    
    pygame.display.update()

pygame.quit() 