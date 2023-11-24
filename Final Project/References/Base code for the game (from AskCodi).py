import pygame
import random

# Initialize the game
pygame.init()

# Define the game window size
window_width = 800
window_height = 600

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Whirlybird")

# Define the player's character
player_size = 50
player_x = window_width // 2
player_y = window_height // 2

# Define the speed of the player
player_speed = 5

# Define the obstacle size and position
obstacle_width = 100
obstacle_height = random.randint(100, 400)
obstacle_x = window_width
obstacle_y = window_height - obstacle_height

# Define the score
score = 0
font = pygame.font.Font(None, 36)

# The game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    game_window.fill(white)

    # Draw the player character
    pygame.draw.rect(game_window, black, (player_x, player_y, player_size, player_size))

    # Draw the obstacle
    pygame.draw.rect(game_window, black, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Move the obstacle towards the player
    obstacle_x -= 5

    # Check for collision with the player
    # Check for collision with the player
    if (player_x < obstacle_x + obstacle_width and
            player_x + player_size > obstacle_x and
            player_y < obstacle_y + obstacle_height and
            player_y + player_size > obstacle_y):
        running = False

    # Increase score if obstacle passed successfully
    if obstacle_x + obstacle_width < 0:
        score += 1
        obstacle_x = window_width
        obstacle_height = random.randint(100, 400)
        obstacle_y = window_height - obstacle_height

    # Display the score
    text = font.render("Score: " + str(score), True, black)
    game_window.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)  # FPS limit, set to 60 frames per second

# Game over
game_window.fill(white)
game_over_text = font.render("Game Over", True, black)
game_window.blit(game_over_text, (window_width // 2 - 80, window_height // 2 - 18))
final_score_text = font.render("Final Score: " + str(score), True, black)
game_window.blit(final_score_text, (window_width // 2 - 100, window_height // 2 + 18))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit the game
pygame.quit()

