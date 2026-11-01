import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

# Load and resize background image
background_image = pygame.image.load("bg.jpg")
background_image = pygame.transform.scale(
    background_image,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Create font
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

# Sprite class
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))

        pygame.draw.rect(
            self.image,
            color,
            pygame.Rect(0, 0, width, height)
        )

        self.rect = self.image.get_rect()

    # Movement function
    def move(self, x_change, y_change):

        self.rect.x = max(
            min(self.rect.x + x_change,
                SCREEN_WIDTH - self.rect.width), 0
        )

        self.rect.y = max(
            min(self.rect.y + y_change,
                SCREEN_HEIGHT - self.rect.height), 0
        )


# Create game screen
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Sprite Collision")

# Create sprite group
all_sprites = pygame.sprite.Group()

# Create first sprite (Player)
sprite1 = Sprite(pygame.Color('black'), 20, 30)

sprite1.rect.x = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width
)

sprite1.rect.y = random.randint(
    0, SCREEN_HEIGHT - sprite1.rect.height
)

# Create second sprite (Target)
sprite2 = Sprite(pygame.Color('red'), 20, 30)

sprite2.rect.x = random.randint(
    0, SCREEN_WIDTH - sprite2.rect.width
)

sprite2.rect.y = random.randint(
    0, SCREEN_HEIGHT - sprite2.rect.height
)

# Add sprites to group
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Game variables
running = True
won = False

clock = pygame.time.Clock()

# Main game loop
while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                running = False

    # Player movement
    if not won:

        keys = pygame.key.get_pressed()

        x_change = (
            keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        ) * MOVEMENT_SPEED

        y_change = (
            keys[pygame.K_DOWN] - keys[pygame.K_UP]
        ) * MOVEMENT_SPEED

        sprite1.move(x_change, y_change)

        # Collision detection
        if sprite1.rect.colliderect(sprite2.rect):

            all_sprites.remove(sprite2)
            won = True

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw sprites
    all_sprites.draw(screen)

    # Display winning message
    if won:

        win_text = font.render(
            "You win!",
            True,
            pygame.Color('black')
        )

        screen.blit(
            win_text,
            (
                (SCREEN_WIDTH - win_text.get_width()) // 2,
                (SCREEN_HEIGHT - win_text.get_height()) // 2
            )
        )

    # Update display
    pygame.display.flip()

    # Set FPS
    clock.tick(90)

# Quit game
pygame.quit()
