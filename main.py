import pygame
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brick Breaker")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BALL_RADIUS = 10
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = 5
ball_dy = -5

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle_x = WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT * 2
paddle_dx = 0

BRICK_WIDTH = 50
BRICK_HEIGHT = 20
BRICKS_PER_ROW = WINDOW_WIDTH // BRICK_WIDTH
BRICK_ROWS = 5
brick_colors = [RED, ORANGE, YELLOW, GREEN, BLUE]
bricks = []

for row in range(BRICK_ROWS):
    brick_row = []
    for col in range(BRICKS_PER_ROW):
        brick_x = col * BRICK_WIDTH
        brick_y = row * BRICK_HEIGHT
        brick_color = brick_colors[row]
        brick_rect = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
        brick_row.append((brick_rect, brick_color))
    bricks.append(brick_row)

def draw_ball():
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)


def draw_paddle():
    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))


def draw_bricks():
    for row in bricks:
        for brick in row:
            if brick[0].x != -BRICK_WIDTH:
                pygame.draw.rect(window, brick[1], brick[0])


def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, paddle_dx, paddle_x

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= BALL_RADIUS or ball_x >= WINDOW_WIDTH - BALL_RADIUS:
        ball_dx = -ball_dx
    if ball_y <= BALL_RADIUS:
        ball_dy = -ball_dy

    if ball_y >= paddle_y - BALL_RADIUS and ball_x >= paddle_x and ball_x <= paddle_x + PADDLE_WIDTH:
        ball_dy = -ball_dy
        ball_dx += paddle_dx

    for row in bricks:
        for brick in row:
            if brick[0].colliderect((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                brick[0].x = -BRICK_WIDTH
                ball_dy = -ball_dy

    if ball_y >= WINDOW_HEIGHT:
        return True

    for row in bricks:
        for brick in row:
            if brick[0].x:
