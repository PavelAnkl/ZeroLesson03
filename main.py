import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon-tir.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/")
target_width = 80
target_height = 80

#рандомное расположение мишение - начальная точка 0, ширина и высота экрана минус размер мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

#рандомный цвет фона в rgb
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

#мишень
target_image = pygame.image.load("img/target.png")

running = True
while running:
    pass


pygame.quit()