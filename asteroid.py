from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_v1 = self.velocity.rotate(random_angle)
        new_v2 = self.velocity.rotate(-random_angle)
        new_r = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_r)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_r)
        asteroid1.velocity = new_v1 * 1.2
        asteroid2.velocity = new_v2 * 1.2