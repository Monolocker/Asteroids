import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time

    # Start infinite game loop 
    while True:
        log_state()
        
        # Event handling, checks for user interactions since last frame
        for event in pygame.event.get():
            # Exit loop if window is closed
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip() # Refresh screen to show updates

        # Limit framerate to 60 FPS
        clock.tick(60) 
        dt = clock.tick(60) / 1000 # Convert from ms to s 

if __name__ == "__main__":
    main()
