import pygame
import random
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Relaxing Snowscape"

class Snow:
    def __init__(self):
        self.size = 5
        self.x = random.randrange(0, SCREEN_WIDTH)
        self.y = 400
        self.width = 10
        self.height = 10
        self.y_vel = 5
        self.colour = WHITE

    def update(self):
        "Updates the location of the snow"
        self.y += self.y_vel

    def rect(self) -> pygame.rect:
        return[self.x, self.y, self.width, self.height]

def main() -> None:
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    done = False
    snow = Snow()
    clock = pygame.time.Clock()
    num_snow = 100
    snow = []
    for i in range(num_snow):
        snow.append(snow())

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # snow.update()

        screen.fill(BLUE)
        pygame.draw.circle(screen, snow.colour (snow.x, snow.y), snow.size)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()