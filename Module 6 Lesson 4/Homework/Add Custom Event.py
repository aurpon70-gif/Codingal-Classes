import pygame
import random

# 1. Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Sprite Color Change")

# 2. Define Sprite Class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        # Generate a random RGB color
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(random_color)

# 3. Create Custom Event and Set Timer
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Fires every 2000 ms (2 seconds)

# 4. Instantiate Sprites and Add to Group
sprite1 = ColorSprite((255, 0, 0), 250, 250)   # Red sprite on the left
sprite2 = ColorSprite((0, 0, 255), 450, 250)   # Blue sprite on the right
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# 5. Main Game Loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Catch the custom event when it fires
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Draw everything
    screen.fill((30, 30, 30))  # Dark background
    all_sprites.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()