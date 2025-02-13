import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x,y,shots_group):
        super().__init__(x,y,PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.shots_group=shots_group
        self.rect = pygame.Rect(x-PLAYER_RADIUS, y-PLAYER_RADIUS, PLAYER_RADIUS*2, PLAYER_RADIUS*2)
        self.timer = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer==0:
                self.shoot()
        self.timer-=dt
        if self.timer<0:
            self.timer=0
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position

    def shoot(self):
        print("Shooting")
        sh = Shot(self.position.x, self.position.y,SHOT_RADIUS)
        sh.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        sh.velocity *= PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
