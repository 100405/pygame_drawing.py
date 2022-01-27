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


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "DVD Screen Saver"

class Dvdimage:
    """Represents a dvdimage on screen

    Attributes:
        x, y coordinates of top-left corner
        width: with of our rectangle in px
        height: height of our rectangle in px
        colour: hex value of rgb"""
    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 180
        self.height = 180
        self.img = pygame.image.load("images1/enemy.png")
        self.x_vel = 5
        self.y_vel = 5

    def rect(self) -> pygame.rect:
        """Returns a pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height]

    def update(self) -> None:
        self.x += self.x_vel
        if self.x < 0:
            self.x = 0
            self.x_vel = -self.x_vel
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.x_vel = -self.x_vel

        self.y += self.y_vel
        if self.y < 0:
            self.y = 0
            self.y_vel = -self.y_vel
        if self.y + self.width > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.width
            self.y_vel = -self.y_vel



def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()
    bg_image = pygame.image.load('images1/uzwq176ixfpslxkgxl1i.webp')

    # Create the main loop
    while not done:
        # Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Logic (Change the environment)
        dvd_image.update()

        # print(f"x: {enemy.png.x}36+ ")

        # Draw the environment
        screen.fill(WHITE)  # fill with bgcolor

        # background
        bg_image = pygame.transform.scale(bg_image, (960, 540))
        screen.blit(bg_image, (0,0))

        # dvdimage
        screen.blit(dvd_image.img , (dvd_image.x, dvd_image.y))

        pygame.display.flip()
        # Tick the clock
        clock.tick(60)
if __name__ == "__main__":
    main()