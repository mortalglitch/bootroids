import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Defining groups:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    # instance player
    player_ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects player controls etc...
        updatable.update(dt)

        screen.fill("black")

        # Draw all drawables
        for thing_to_draw in drawable:
            thing_to_draw.draw(screen)
        pygame.display.flip()

        # End of loop actions
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
