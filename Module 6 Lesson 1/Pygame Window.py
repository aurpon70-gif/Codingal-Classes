# Import Library
import pygame
# Initialize Pygame
pygame.init()
# Create a Pygame Window
screen = pygame.display.set_mode((400, 500))
# Create a loop to keep the window open
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Make the changes able to be seen
        pygame.display.flip()