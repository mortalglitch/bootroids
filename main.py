import pygame
import sys

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Defining groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    # instance objects
    player_ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects player controls etc...
        updatable.update(dt)

        # Collision check for player
        for current_asteroid in asteroids:
            if current_asteroid.is_colliding(player_ship):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        # Draw all drawables
        for thing_to_draw in drawable:
            thing_to_draw.draw(screen)
        pygame.display.flip()

        # End of loop actions
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
