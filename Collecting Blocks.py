# Collecting Blocks Example
# Author: Ubial

import time
import random
import pygame

pygame.init()

WHITE =     (255, 255, 255)
BLACK =     (  0,   0,   0)
RED   =     (255,   0,   0)
GREEN =     (  0, 255,   0)
BLUE  =     (  0,   0, 255)
ETON_BLUE = (135, 187, 162)
RAD_RED =   (255,  56, 100)
BLK_CHOCOLATE = (25, 17, 2)

BGCOLOUR =  WHITE

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecing Blocks"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite
    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.image.load("./images1/download-1.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

        self.hp = 300
    def hp_remaining(self) -> float:
        return float(self.hp / 300)



class Block(pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite.Sprite
    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
    """
    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r, g, b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images1/underage_girl.jpg")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])


    def update(self) -> None:
        """Calculate Movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Constrain Movement
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    num_enemies = 10
    score = 0
    time_start = time.time()
    time_invincible = 5             # seconds
    game_state = "running"
    endgame_cooldown = 5            # seconds
    time_ended = 0.0

    endgame_messages = {
        "win": "Congratulations, you won!",
        "lose": "Sorry, they got you. Play again!",
    }

    font = pygame.font.SysFont("Arial", 25)

    pygame.mouse.set_visible(False)

    # Create groups to hold Sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # Create all the block sprites and add to block_sprites
    for i in range(num_blocks):
        # Create a block (set its parameters)
        block = Block(BLACK, 20, 15)

        # Set a random location for the block inside the screen
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)

        # Add the block to the block_sprites Group
        # Add the block to the all_sprites Group
        block_sprites.add(block)
        all_sprites.add(block)

    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()

        # Add it to the sprites list (enemy_sprites and all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    # Create the Player block
    player = Player()
    # Add the Player to all_sprites group
    all_sprites.add(player)

    pygame.mouse.set_visible(True)


    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # End-game listener
        if score == num_blocks:
            # Indicate to draw a message
            game_state = "won"

            # SET THE TIME THAT THE GAME WAS WON
            if time_ended == 0:
                time_ended = time.time()

            # Set parameters to keep the screen alive
            # Wait 5 seconds to kill the screen
            if time.time() - time_ended >= endgame_cooldown:
                done = True

        if player.hp_remaining() <= 0:
            done = True

        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2

        # Update the location of all sprites
        all_sprites.update()

        # Check all collisions between player and the ENEMIES
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # Set a time for invincibility at the beginning of the game
        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                player.hp -= 1

            # Check all collisions between player and the blocks
            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

            for block in blocks_collided:
                score += 1

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)

        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )

        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, GREEN, [580, 5, 115, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 115 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLUE, [580, 5, life_remaining, 20])

        # If we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, BLACK),
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            )

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()