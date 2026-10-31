import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions (width, height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Sprites Example")

# Define colors (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite 1 (Controlled with arrow keys)
sprite1_x = 100
sprite1_y = 100
sprite1_width = 50
sprite1_height = 50
sprite1_speed = 5

# Sprite 2 (Stationary rectangular sprite)
sprite2_x = 400
sprite2_y = 300
sprite2_width = 80
sprite2_height = 60

# Main game loop clock
clock = pygame.time.Clock()

# Game loop
while True:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # 2. Handle Continuous Keyboard Input for Sprite 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1_x -= sprite1_speed
    if keys[pygame.K_RIGHT]:
        sprite1_x += sprite1_speed
    if keys[pygame.K_UP]:
        sprite1_y -= sprite1_speed
    if keys[pygame.K_DOWN]:
        sprite1_y += sprite1_speed

    # Keep Sprite 1 within screen boundaries
    sprite1_x = max(0, min(sprite1_x, SCREEN_WIDTH - sprite1_width))
    sprite1_y = max(0, min(sprite1_y, SCREEN_HEIGHT - sprite1_height))

    # 3. Drawing / Rendering
    screen.fill(WHITE) # Clear screen with a white background

    # Draw Sprite 1 (Red rectangle)
    pygame.draw.rect(screen, RED, (sprite1_x, sprite1_y, sprite1_width, sprite1_height))

    # Draw Sprite 2 (Blue rectangle)
    pygame.draw.rect(screen, BLUE, (sprite2_x, sprite2_y, sprite2_width, sprite2_height))

    # 4. Update Display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)