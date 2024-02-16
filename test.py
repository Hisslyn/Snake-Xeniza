import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, 100, 50))  # Draw simple rectangle
    pygame.display.flip()  # Refresh game screen
    
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
