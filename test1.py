import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Moving Rectangle')

# Colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)

# Rectangle properties
rect_x = 50
rect_y = 50
rect_width = 100
rect_height = 50
rect_speed = 5  # Pixels per frame

# Set the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Move the rectangle
    rect_x += rect_speed
    # If the rectangle goes off the screen, reset its position
    if rect_x > screen_width:
        rect_x = -rect_width

    # Draw the rectangle
    pygame.draw.rect(screen, green, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
