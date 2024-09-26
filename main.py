import sys
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for upd in updatable:
            upd.update(dt)
        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if ast.collision(bullet):
                    bullet.kill()
                    ast.split()

        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
