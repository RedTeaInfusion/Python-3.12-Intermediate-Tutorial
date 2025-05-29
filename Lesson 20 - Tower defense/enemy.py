import pygame
import math
from constants import GRID, CELL_SIZE, RED, GREEN

class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, speed, value, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)          
        self.rect = self.image.get_rect()
        self.rect.topleft = self.find_path(GRID)[0]
        self.rect.x *= CELL_SIZE
        self.rect.y *= CELL_SIZE
        self.speed = speed
        self.value = value
        self.path_index = 0
        self.health = health
        self.max_health = health
        
    def find_path(self, grid):
        path = []
        start = None
        for y, row in enumerate(grid):
            if 2 in row:
                start = (row.index(2), y)
                break
        current = start
        while current:
            path.append(current)
            x, y = current
            if grid[y][x] == 3:
                break
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] in [1, 3] and (nx, ny) not in path:
                    current = (nx, ny)
                    break
            else:
                current = None
        return path

    def progress_path(self, path):
        if self.path_index < len(path) - 1:
            target = (path[self.path_index + 1][0] * CELL_SIZE,
                      path[self.path_index + 1][1] * CELL_SIZE)
            dx, dy = target[0] - self.rect.x, target[1] - self.rect.y
            distance = math.hypot(dx, dy)
            if distance < self.speed:
                self.path_index += 1
            else:
                dx, dy = dx / distance, dy / distance
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
        return self.path_index == len(path) - 1

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y - 10, CELL_SIZE, 5))
        normalized_health = self.health / self.max_health
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y - 10, CELL_SIZE * normalized_health, 5))