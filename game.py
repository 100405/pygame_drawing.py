import pygame

# constants
white = (255, 255, 255)
black = (0, 0, 0)

# dimensions
width = 600
height = 600

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('8 Bong')

delay = 30
score = 0

font = pygame.font.SysFont('sans', 16)

paddle_speed = 20

paddle_width = 10
paddle_height = 100

# Creating paddles/players and their positions at the start of the game
player1_x_pos = 10
player1_y_pos = height / 2 - paddle_height / 2

player2_x_pos = width - paddle_width - 10
player2_y_pos = height / 2 - paddle_height / 2

#Player score
player1_score = 0
player2_score = 0

#Player Movements
player1_up = False
player1_down = False
player2_up = False
player2_down = False

#Creating the ball and their positions
ball_x_pos = width / 2
ball_y_pos = height / 2
ball_width = 3
ball_x_vel = -5
ball_y_vel = 0

#Drawing the screen
screen = pygame.display.set_mode((width, height))
#Drawing objects
def draw_objects():
    pygame.draw.rect(screen, white, (int(player1_x_pos), int(player1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (int(player2_x_pos), int(player2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
    screen.blit(font.render(str(player2_score), False, white), (width / 2.5, 30))
    screen.blit(font.render(str(player1_score), False, white), (width / 1.5, 30))

#Player Movements
def apply_player_movement():
    global player1_y_pos
    global player2_y_pos

    if player1_up:
        player1_y_pos = max(player1_y_pos - paddle_speed, 0)
    elif player1_down:
        player1_y_pos = min(player1_y_pos + paddle_speed, height)
    if player2_up:
        player2_y_pos = max(player2_y_pos - paddle_speed, 0)
    elif player2_down:
        player2_y_pos = min(player2_y_pos + paddle_speed, height)

#Ball Movements
def apply_ball_movement():
        global ball_x_pos
        global ball_y_pos
        global ball_x_vel
        global ball_y_vel
        global player1_score
        global player2_score

        # Changing the score of the players when a "goal" is scored
        if (ball_x_pos + ball_x_vel < player1_x_pos + paddle_width) and (player1_y_pos < ball_y_pos + ball_y_vel + ball_width < player1_y_pos + paddle_height):
            ball_x_vel = -ball_x_vel
            ball_y_vel = (player1_y_pos + paddle_height / 2 - ball_y_pos) / 15
            ball_y_vel = -ball_y_vel
        elif ball_x_pos + ball_x_vel < 0:
            player2_score += 1
            ball_x_pos = width / 2
            ball_y_pos = height / 2
            ball_x_vel = 10
            ball_y_vel = 0
        if (ball_x_pos + ball_x_vel > player2_x_pos - paddle_width) and (player2_y_pos < ball_y_pos + ball_y_vel + ball_width < player2_y_pos + paddle_height):
            ball_x_vel = -ball_x_vel
            ball_y_vel = (player2_y_pos + paddle_height / 2 - ball_y_pos) / 15
            ball_y_vel = -ball_y_vel
        elif ball_x_pos + ball_x_vel > height:
            player1_score += 1
            ball_x_pos = width / 2
            ball_y_pos = height /2
            ball_x_vel = -10
            ball_y_vel = 0
        if ball_x_pos + ball_y_vel > height or ball_y_pos + ball_y_vel < 0:
            ball_y_vel = -ball_y_vel

        ball_x_pos += ball_x_vel
        ball_y_pos += ball_y_vel

screen.fill(black)
pygame.display.flip()

#Player Controls
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                player1_up = True
            if event.key == pygame.K_s:
                player1_down = True
            if event.key == pygame.K_UP:
                player2_up = True
            if event.key == pygame.K_DOWN:
                player2_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_up = False
            if event.key == pygame.K_s:
                player1_down = False
            if event.key == pygame.K_UP:
                player2_up = False
            if event.key == pygame.K_DOWN:
                player2_down = False

    screen.fill(black)
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    clock.tick(75)














