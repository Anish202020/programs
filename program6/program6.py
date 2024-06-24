import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moving Circle Animation')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initial position of the circle
x, y = width // 2, height // 2
radius = 20
dx, dy = 5, 5  # Movement step

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the circle
    x += dx
    y += dy

    # Bounce the circle off the edges
    if x - radius < 0 or x + radius > width:
        dx = -dx
    if y - radius < 0 or y + radius > height:
        dy = -dy

    # Fill the screen with black
    window.fill(black)

    # Draw the circle
    pygame.draw.circle(window, white, (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
