import pygame
import sys
import subprocess
pygame.init()

wwidth , hhieght = 600,600

screen2 = pygame.display.set_mode((600,600))
screen2.fill('cyan')
start = pygame.Surface((300 , 40))
start.fill('green')
start_rect = start.get_frect(center = ((300, 200)))
customize = pygame.Surface((300 , 40))
customize.fill('yellow')
customize_rect = customize.get_frect(center = ((300, 300)))
font = pygame.font.Font(None, 40)
label1 = font.render('START' , True , 'black')
running = True

while running:
    for events in pygame.event.get():
           if events.type == pygame.QUIT:
            running = False
           if events.type == pygame.MOUSEBUTTONDOWN:
             if start_rect.collidepoint(events.pos):

              subprocess.Popen([sys.executable, "main.py"])
              running = False
           
    screen2.blit(start, start_rect)
    screen2.blit(customize, customize_rect)
    screen2.blit(label1, label1.get_frect(center = ((300, 200))) )
    pygame.display.update()

pygame.quit() 