
import math
import random
import pygame

# =====================================
# 1. CONSTANTS
# =====================================

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_WIDTH = 55
PLAYER_HEIGHT = 55

ENEMY_WIDTH = 45
ENEMY_HEIGHT = 45

BULLET_WIDTH = 8
BULLET_HEIGHT = 18

PLAYER_START_X = 370
PLAYER_START_Y = 420

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 3
ENEMY_SPEED_Y = 35

BULLET_SPEED_Y = 8

# =====================================
# 2. INITIALIZE PYGAME
# =====================================

pygame.init()

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

# =====================================
# 3. BACKGROUND
# =====================================

background = pygame.image.load(
    'background.png'
).convert()

background = pygame.transform.scale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# =====================================
# 4. GAME ICON
# =====================================

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# =====================================
# 5. PLAYER
# =====================================

playerImg = pygame.image.load(
    'player.png'
).convert_alpha()

playerImg = pygame.transform.scale(
    playerImg,
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# =====================================
# 6. ENEMY
# =====================================

enemyImg = []
enemyX = []
enemyY = []

enemyX_change = []
enemyY_change = []

num_of_enemies = 6

# Resize enemy image
enemy_image = pygame.image.load(
    'enemy.png'
).convert_alpha()

enemy_image = pygame.transform.scale(
    enemy_image,
    (ENEMY_WIDTH, ENEMY_HEIGHT)
)

for i in range(num_of_enemies):

    enemyImg.append(enemy_image)

    enemyX.append(
        random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
    )

    enemyY.append(
        random.randint(
            ENEMY_START_Y_MIN,
            ENEMY_START_Y_MAX
        )
    )

    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# =====================================
# 7. BULLET
# =====================================

bulletImg = pygame.image.load(
    'bullet.png'
).convert_alpha()

bulletImg = pygame.transform.scale(
    bulletImg,
    (BULLET_WIDTH, BULLET_HEIGHT)
)

bulletX = 0
bulletY = PLAYER_START_Y

bulletY_change = BULLET_SPEED_Y

bullet_state = "ready"

# =====================================
# 8. SCORE
# =====================================

score_value = 0

font = pygame.font.Font(
    'freesansbold.ttf',
    32
)

textX = 10
textY = 10

# Game Over Font
over_font = pygame.font.Font(
    'freesansbold.ttf',
    64
)

# =====================================
# 9. DISPLAY SCORE
# =====================================

def show_score(x, y):

    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(score, (x, y))


# =====================================
# 10. GAME OVER TEXT
# =====================================

def game_over_text():

    over_text = over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    screen.blit(
        over_text,
        (200, 230)
    )


# =====================================
# 11. PLAYER FUNCTION
# =====================================

def player(x, y):

    screen.blit(
        playerImg,
        (x, y)
    )


# =====================================
# 12. ENEMY FUNCTION
# =====================================

def enemy(x, y, i):

    screen.blit(
        enemyImg[i],
        (x, y)
    )


# =====================================
# 13. FIRE BULLET
# =====================================

def fire_bullet(x, y):

    global bullet_state

    bullet_state = "fire"

    screen.blit(
        bulletImg,
        (x, y)
    )


# =====================================
# 14. COLLISION DETECTION
# =====================================

def isCollision(enemyX, enemyY, bulletX, bulletY):

    enemy_rect = pygame.Rect(
        enemyX,
        enemyY,
        ENEMY_WIDTH,
        ENEMY_HEIGHT
    )

    bullet_rect = pygame.Rect(
        bulletX,
        bulletY,
        BULLET_WIDTH,
        BULLET_HEIGHT
    )

    return enemy_rect.colliderect(bullet_rect)


# =====================================
# 15. GAME LOOP
# =====================================

running = True
game_over = False

while running:

    # Background
    screen.blit(background, (0, 0))

    # =================================
    # EVENT HANDLING
    # =================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if not game_over:

                if event.key == pygame.K_LEFT:

                    playerX_change = -5

                if event.key == pygame.K_RIGHT:

                    playerX_change = 5

                if (
                    event.key == pygame.K_SPACE
                    and bullet_state == "ready"
                ):

                    bulletX = (
                        playerX
                        + PLAYER_WIDTH // 2
                        - BULLET_WIDTH // 2
                    )

                    bulletY = playerY

                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:

            if event.key in [
                pygame.K_LEFT,
                pygame.K_RIGHT
            ]:

                playerX_change = 0

    # =================================
    # PLAYER MOVEMENT
    # =================================

    if not game_over:

        playerX += playerX_change

        playerX = max(
            0,
            min(
                playerX,
                SCREEN_WIDTH - PLAYER_WIDTH
            )
        )

        # =================================
        # BULLET MOVEMENT
        # =================================

        if bullet_state == "fire":

            bulletY -= bulletY_change

            if bulletY < 0:

                bulletY = PLAYER_START_Y
                bullet_state = "ready"

        # =================================
        # ENEMY MOVEMENT
        # =================================

        for i in range(num_of_enemies):

            # Game Over Condition
            if enemyY[i] + ENEMY_HEIGHT >= playerY:

                game_over = True
                break

            # Move Enemy
            enemyX[i] += enemyX_change[i]

            # Screen Boundary Check
            if (
                enemyX[i] <= 0
                or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH
            ):

                enemyX_change[i] *= -1

                enemyY[i] += enemyY_change[i]

            # =================================
            # COLLISION CHECK
            # =================================

            if bullet_state == "fire":

                if isCollision(
                    enemyX[i],
                    enemyY[i],
                    bulletX,
                    bulletY
                ):

                    bulletY = PLAYER_START_Y

                    bullet_state = "ready"

                    score_value += 1

                    # Reset Enemy Position
                    enemyX[i] = random.randint(
                        0,
                        SCREEN_WIDTH - ENEMY_WIDTH
                    )

                    enemyY[i] = random.randint(
                        ENEMY_START_Y_MIN,
                        ENEMY_START_Y_MAX
                    )

            # Draw Enemy
            enemy(enemyX[i], enemyY[i], i)

        # =================================
        # DRAW BULLET
        # =================================

        if bullet_state == "fire":

            fire_bullet(bulletX, bulletY)

    else:

        game_over_text()

        # Draw remaining enemies
        for i in range(num_of_enemies):

            enemy(enemyX[i], enemyY[i], i)

    # =================================
    # DRAW PLAYER AND SCORE
    # =================================

    player(playerX, playerY)

    show_score(textX, textY)

    # Update Screen
    pygame.display.update()

    # FPS
    clock.tick(60)


# =====================================
# 16. QUIT GAME
# =====================================