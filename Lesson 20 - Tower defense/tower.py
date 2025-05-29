import pygame
import math
from projectile import Projectile

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, level, damage, fire_range, fire_rate, cost, upgrade_cost, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.level = level
        self.damage = damage
        self.fire_range = fire_range
        self.fire_rate = fire_rate
        self.fire_rate_counter = 200
        self.cost = cost
        self.upgrade_cost = upgrade_cost
        
    def update(self, enemies):
        self.fire_rate_counter -= 1
        if self.fire_rate_counter <= self.fire_rate:
            target = self.find_target(enemies)
            if target:
                self.fire_rate_counter = 200
                return Projectile(self.rect.centerx, self.rect.centery, self.damage, target)
        return None
    
    def find_target(self, enemies):
        for enemy in enemies:
            distance = math.hypot(enemy.rect.centerx - self.rect.centerx, 
                                  enemy.rect.centery - self.rect.centery)
            if distance <= self.fire_range:
                return enemy
        return None