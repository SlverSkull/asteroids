import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from projectile import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable,)
    Projectile.containers = (updateable, drawable, projectiles)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for sprite in updateable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for sprite_a in asteroids:
            if sprite_a.collision(player):
                print("Game over!")
                exit()
            for sprite_p in projectiles:
                if sprite_p.collision(sprite_a):
                    sprite_a.split()
                    sprite_p.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
