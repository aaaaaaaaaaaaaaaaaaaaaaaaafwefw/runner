import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vertical Runner")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Игрок
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70
player_speed = 5

# Препятствия
obstacle_width, obstacle_height = 50, 50
obstacles = []
for _ in range(5):  # Reduced number of obstacles
    x = random.randint(0, WIDTH - obstacle_width)
    y = random.randint(-200, -40)  # Increased negative range for initial y position
    speed = random.randint(3, 7)  # Adjusted speed range
    obstacles.append([x, y, speed])

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление состояния игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Обновление состояния препятствий
    for obs in obstacles:
        obs[1] += obs[2]
        if obs[1] > HEIGHT:
            obs[0] = random.randint(0, WIDTH - obstacle_width)
            obs[1] = random.randint(-200, -40)
            obs[2] = random.randint(3, 7)

    # Проверка на столкновения
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for obs in obstacles:
        obs_rect = pygame.Rect(obs[0], obs[1], obstacle_width, obstacle_height)
        if player_rect.colliderect(obs_rect):
            running = False

    # Отрисовка
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, player_rect)
    for obs in obstacles:
        pygame.draw.rect(win, RED, (obs[0], obs[1], obstacle_width, obstacle_height))
    pygame.display.flip()

pygame.quit()
