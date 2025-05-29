import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, target):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.damage = damage
        self.target = target
        self.speed = 5

    def update(self):
        if self.target.alive():
            dx = self.target.rect.centerx - self.rect.centerx
            dy = self.target.rect.centery - self.rect.centery
            distance = math.hypot(dx, dy)
            if distance > 0:
                dx, dy = dx / distance, dy / distance
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
            if self.rect.colliderect(self.target.rect):
                self.target.health -= self.damage
                self.kill()
        else:
            self.kill()