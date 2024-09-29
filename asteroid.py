from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.score += 1
            return
        random_angle = random.uniform(20, 50)
        velo_p = self.velocity.rotate(random_angle)
        velo_n = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster_p = Asteroid(self.position.x, self.position.y, new_radius)
        aster_p.velocity = 1.2 * velo_p
        aster_n = Asteroid(self.position.x, self.position.y, new_radius)
        aster_n.velocity = 1.2 * velo_n
