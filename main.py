# Pygame Drawing
# Author : Tony Lwe
# 9 November 2021

# Get introduced to Pygame and draw objects on screen

import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"
def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # Create the main loop
    while not done:
        # Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Logic (Change the environment)

        # Draw the environment
            screen.fill(WHITE)  # fill with bgcolor
        # Update the screen
            pygame.display.flip()
        # Tick the clock
        clock.tick(60)
if __name__ == "__main__":
    main()