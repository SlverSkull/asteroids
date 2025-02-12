import pygame
from circleshape import *
from constants import *

class Projectile(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position = self.position + self.velocity * dt * PROJECTILE_SPEED
