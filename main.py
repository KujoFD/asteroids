# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field= AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if ast.check_collision(p1)==True:
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
