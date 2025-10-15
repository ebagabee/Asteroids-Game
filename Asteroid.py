from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self):
        pygame.draw.circle(self.position, self.radius, 2)

    def update(self, dt):
        return self.velocity * dt