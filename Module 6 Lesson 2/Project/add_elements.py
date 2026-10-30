import pygame

# Initialize Pygame
pygame.init()

# 1. Window size (640, 480)
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 2. Set caption - My first game screen
pygame.display.set_caption("My first game screen")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # You can change this to any color of your choice

# Setup font for displaying text
font = pygame.font.Font(None, 36)
text_surface = font.render("Hello Pygame!", True, (0, 0, 0))  # Black text for visibility
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

# Rectangle parameters (positioned at the center of the screen)
rect_width, rect_height = 150, 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2 - 50
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main game loop
running = True
while running:
  # Handle events (allows closing the window)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # 5. The background colour of the screen - White (0, 0, 0) -> Wait, prompt says White, let's use (255, 255, 255)
  screen.fill((255, 255, 255))

  # 3. Create a rectangle of the colour of your choice, positioned at the centre of the screen
  pygame.draw.rect(screen, BLUE, rect)

  # 4. Display a text on the screen
  screen.blit(text_surface, text_rect)

  # Update the display
  pygame.display.flip()

# Quit Pygame properly
pygame.quit()