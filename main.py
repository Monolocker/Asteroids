import pygame
import sys
from constants import * 
from logger import log_state, log_event
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add Player class to groups before player object instance creation
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate player object

    # Add asteroid to groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Create AsteroidField object
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # Start infinite game loop 
    while True:
        log_state()

        # Event handling
        for event in pygame.event.get():
            # Exit loop if window is closed
            if event.type == pygame.QUIT:
                return

        # Update, then render
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() # Refresh screen 

        # Limit framerate to 60 FPS, convert ms to s
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
