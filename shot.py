import pygame
from circleshape import CircleShape
from constants import *
class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius=radius

    def update(self,dt):
        self.position += self.velocity *dt

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius)
