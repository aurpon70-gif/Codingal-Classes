import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My first game screen")

GREY = (58, 58, 58)

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (300, 300))

image_x = (screen_width - 300) // 2
image_y = (screen_height - 300) // 2

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(GREY)

  screen.blit(image, (image_x, image_y))

  pygame.display.flip()

pygame.quit()