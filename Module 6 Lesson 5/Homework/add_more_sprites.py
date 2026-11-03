import random
import pygame

# Initialize Pygame
pygame.init()

# Constants for Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Add More Sprites")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()


# Player Class
class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((40, 40))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.centerx = SCREEN_WIDTH // 2
    self.rect.bottom = SCREEN_HEIGHT - 20
    self.speed = 5

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.rect.left > 0:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
      self.rect.x += self.speed
    if keys[pygame.K_UP] and self.rect.top > 0:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
      self.rect.y += self.speed


# Enemy Class
class Enemy(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((30, 30))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    # Position randomly on the screen
    self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
    self.rect.y = random.randint(50, SCREEN_HEIGHT // 2)


# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create Player
player = Player()
all_sprites.add(player)

# Create 7 Enemy Sprites positioned randomly
for i in range(7):
  enemy = Enemy()
  all_sprites.add(enemy)
  enemies.add(enemy)

# Score variable
score = 0
font = pygame.font.SysFont(None, 36)

# Game Loop
running = True
while running:
  # Event Handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update
  all_sprites.update()

  # Check for collisions between player and enemy sprites
  # pygame.sprite.spritecollide drops the collided enemy and increases score
  hit_enemies = pygame.sprite.spritecollide(player, enemies, True)
  for hit in hit_enemies:
    score += 1
    # Respawn a new enemy when one is collected/collided
    new_enemy = Enemy()
    all_sprites.add(new_enemy)
    enemies.add(new_enemy)

  # Drawing / Rendering
  screen.fill(BLACK)
  all_sprites.draw(screen)

  # Render Score
  score_text = font.render(f"Score: {score}", True, WHITE)
  screen.blit(score_text, (10, 10))

  # Refresh Screen
  pygame.display.flip()
  clock.tick(60)

pygame.quit()