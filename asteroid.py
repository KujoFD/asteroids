import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius=radius
        if not hasattr(self,"velocity"):
            self.velocity = pygame.math.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        print(f"Starting split. Original velocity: {self.velocity}") #Debug Print
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        ang=random.uniform(20,50)

        #Create new velocity vectors while preserving magnitude
        current_speed = self.velocity.length() #get current speed
        left_ang=self.velocity.rotate(-ang).normalize() * current_speed
        right_ang=self.velocity.rotate(ang).normalize() * current_speed

        new_rad=self.radius-ASTEROID_MIN_RADIUS
        left_ast= Asteroid(self.position.x, self.position.y, new_rad)
        left_ast.velocity = left_ang*1.2
        right_ast =  Asteroid(self.position.x, self.position.y, new_rad)
        right_ast.velocity = right_ang*1.2

        print(f"New velociities: {left_ast.velocity}, {right_ast.velocity}") #Debug print

        for group in self.groups():
            group.add(left_ast)
            group.add(right_ast)
