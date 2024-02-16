import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Snake Xeniza')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10
direction = 'RIGHT'
change_to = direction

# Food properties
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True

# Initialize score
score = 0
# Set the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Key press events to change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    # Update the direction based on the change_to value
    direction = change_to

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= snake_speed
    elif direction == 'DOWN':
        snake_pos[1] += snake_speed
    elif direction == 'LEFT':
        snake_pos[0] -= snake_speed
    elif direction == 'RIGHT':
        snake_pos[0] += snake_speed

    # Insert new position in front of the snake body to simulate movement
    new_head = [snake_pos[0], snake_pos[1]]
    snake_body.insert(0, new_head)

    # Snake eating food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    # Snake collision with boundaries
    if snake_pos[0] >= screen_width or snake_pos[0] < 0 or snake_pos[1] >= screen_height or snake_pos[1] < 0:
        running = False  # End the game

    # Snake collision with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            running = False  # End the game

    # Fill the screen with black background
    screen.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
    # Draw food
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render('Score: ' + str(score), True, white)
    screen.blit(score_text, [0, 0])

    # Refresh game screen
    pygame.display.flip()

    # Frame Per Second /Refresh Rate
    clock.tick(20)

pygame.quit()
sys.exit()
