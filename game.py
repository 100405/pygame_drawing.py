import pygame

#constants
white = (255, 255, 255)
black = (0, 0, 0)

#dimensions
width = 600
height = 600

pygame.init()

delay = 30
score = 0

paddle_speed = 20

paddle_width = 10
paddle_height = 100

#Creating paddles/players and their positions at the start of the game
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
ball_width = 0
ball_x_vel = -5
ball_y_vel = 0

#Drawing the screen
screen = pygame.display.set_mode((width, height))
#Drawing objects
def draw_objects():
    pygame.draw.rect(screen, white, (int(player1_x_pos), int(player1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (int(player2_x_pos), int(player2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
    screen.blit(score, (width / 2, 30))

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
            ball_y_vel = (player2_y_pos = paddle_height / 2 - ball_y_pos) / 15
            ball_y_vel = -ball_y_vel
        elif ball











