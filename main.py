import pygame
from constants import * 
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate player object
    dt = 0 # Delta time

    # Start infinite game loop 
    while True:
        log_state()

        # Event handling
        for event in pygame.event.get():
            # Exit loop if window is closed
            if event.type == pygame.QUIT:
                return

        # Update, then render
        player.update(dt)

        screen.fill("black")
        player.draw(screen) # Re-render player on screen each frame
        pygame.display.flip() # Refresh screen to show updates

        # Limit framerate to 60 FPS, convert ms to s
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
