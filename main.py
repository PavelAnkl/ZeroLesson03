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

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

clock = pygame.time.Clock()

# Инициализация счётчиков попаданий и промахов
hits = 0
misses = 0

# Время последнего обновления мишени
last_update_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(color)

    current_time = pygame.time.get_ticks()
    # Проверяем, прошло ли 3 секунды (3000 миллисекунд) с момента последнего обновления
    if current_time - last_update_time > 3000:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        last_update_time = current_time
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                hits += 1  # Увеличиваем счётчик попаданий
            else:
                misses += 1  # Увеличиваем счётчик промахов

    screen.blit(target_image, (target_x, target_y))

    # Отображение счёта
    font = pygame.font.SysFont(None, 36)
    hits_text = font.render(f'Попаданий: {hits}', True, (0, 255, 0))
    misses_text = font.render(f'Промахов: {misses}', True, (255, 0, 0))
    screen.blit(hits_text, (10, 10))
    screen.blit(misses_text, (10, 50))

    pygame.display.update()

    clock.tick(60)  # Устанавливаем FPS на 60 для плавного обновления

pygame.quit()
