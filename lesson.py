import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon-tir.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

#рандомное расположение мишение - начальная точка 0, ширина и высота экрана минус размер мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

#рандомный цвет фона в rgb
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    #заливка экрана, цвет из переменной color
    screen.fill(color)
    # event — это переменная, в которой у нас будут сохраняться все события
    # pygame.event.get — компонент для работы с событиями, собирающий все события в коллекцию
    for event in pygame.event.get():
        # нажатие на крестик
        if event.type == pygame.quit:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    #отрисовка мишени
    screen.blit(target_image, (target_x, target_y))
    #обновление экрана
    pygame.display.update()

pygame.quit()