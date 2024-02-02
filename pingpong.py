import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20
WHITE = (255, 255, 255)
FPS = 70

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PingPong by gomeroboom")

# Fonts
font = pygame.font.SysFont("couriernew", 35)

# Game variables
ball_speed = 7
paddle_speed = 9
score_player1 = 0
score_player2 = 0

# Create paddles and ball
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_direction = random.choice([1, -1]), random.choice([1, -1])

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed

    # Player 2 controls
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle_speed

    # Move the ball
    ball.x += ball_speed * ball_direction[0]
    ball.y += ball_speed * ball_direction[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction = (ball_direction[0], -ball_direction[1])

    # Ball collisions with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_direction = (-ball_direction[0], ball_direction[1])
        ball_speed += 1

    # Check for scoring
    if ball.left <= 0:
        score_player2 += 1
        ball_speed = 7
        ball_direction = random.choice([1, -1]), random.choice([1, -1])
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2

    if ball.right >= WIDTH:
        score_player1 += 1
        ball_speed = 7
        ball_direction = random.choice([1, -1]), random.choice([1, -1])
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2

    # Clear the screen
    # screen.fill((0, 0, 0))
    bg = pygame.image.load("./background.jpg")
    screen.blit(bg, (0,0))
    # Draw paddles and ball
    pygame.draw.rect(screen, (210, 70, 245), paddle1)
    pygame.draw.rect(screen, (210, 70, 245), paddle2)
    pygame.draw.ellipse(screen, (210, 70, 245), ball)

    # Draw scores
    score_text = font.render(f"{score_player1} - {score_player2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 550))
    # sceen.fill()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
