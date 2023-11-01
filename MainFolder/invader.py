import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
GREEN = (7, 189, 32)
GRAY = (169, 169, 169)

# Create the Pygame window and set the app's name at the top
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invaders")

# Load and play the soundtrack
pygame.mixer.music.load('MainFolder/sounds/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Volume control
volume_step = 0.1

# Define menu options
menu_options = ["Start Game", "Settings", "Exit"]
selected_option = None

# Menu fonts
MENU_FONT = pygame.font.SysFont("comicsansms", 75)
MENU_TITLE_FONT = pygame.font.SysFont("comicsansms", 50)
MENU_NAME_FONT = pygame.font.SysFont("comicsansms", 40)

# Load background image
background = pygame.image.load('MainFolder/images/backg.png')

# Main menu titles and buttons
def draw_menu():
    screen.blit(background, (0, 0))
    title_text = MENU_TITLE_FONT.render("ALIEN INVADERS", True, GREEN)
    title_name = MENU_NAME_FONT.render("By Hamza & Tayyab", True, GREEN)

    screen.blit(title_text, (WIDTH // 5 - title_text.get_width() // 100, 17))
    screen.blit(title_name, (WIDTH // 4 - title_name.get_width() // 600, 90))

    for i, option in enumerate(menu_options):
        text = MENU_FONT.render(option, True, GREEN if selected_option == i else GRAY)
        text_rect = text.get_rect(center=(WIDTH // 2, 250 + i * 100))
        screen.blit(text, text_rect)

# Main menu logic
def main_menu():
    global selected_option
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for i, option in enumerate(menu_options):
                    text_rect = MENU_FONT.render(option, True, GREEN).get_rect(center=(WIDTH // 2, 300 + i * 60))
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        selected_option = i
                        break
                else:
                    selected_option = None
            if event.type == pygame.MOUSEBUTTONDOWN and selected_option is not None:
                if selected_option == 0:
                    # Start the game
                    start_game()
                elif selected_option == 1:
                    # Open settings
                    settings_menu()
                elif selected_option == 2:
                    pygame.quit()

        draw_menu()
        pygame.display.flip()

# Game code
def start_game():
    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, h):
        screen.blit(enemyImg[h], (x, y))

    def fire_bullet(x, y):
        nonlocal bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False

    def show_score(x, y):
        score = font.render("Score: " + str(score_value), True, (125, 225, 225))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (125, 225, 225))
        screen.blit(over_text, (200, 250))

    # Initialize the game
    playerImg = pygame.image.load("MainFolder/images/spaceship.png")
    playerX = 370
    playerY = 480
    playerX_change = 0

    # Enemy
    num_of_enemies = 5
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []

    for h in range(num_of_enemies):
        enemyImg.append(pygame.image.load("MainFolder/images/alien-2.png"))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(1)  # Slower horizontal movement
        enemyY_change.append(40)  # Adjusted vertical movement

    # Bullet
    bulletImg = pygame.image.load("MainFolder/images/bullet-4.png")
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 2
    bullet_state = "ready"

    score_value = 0
    font = pygame.font.Font(None, 36)
    textX = 10
    textY = 10

    over_font = pygame.font.Font(None, 48)

    # Game loop and event handler
    running = True
    while running:
        screen.fill((32, 32, 32))
        # Background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_change = -2
        if keys[pygame.K_RIGHT]:
            playerX_change = 2
        if keys[pygame.K_ESCAPE]:
            if bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        playerX += playerX_change
        if playerX < 0:
            playerX = 0
        elif playerX > 733:
            playerX = 733

        # Enemy movement
        for h in range(num_of_enemies):
            if enemyY[h] > 450:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            enemyX[h] += enemyX_change[h]
            if enemyX[h] <= 0:
                enemyX_change[h] = 2
                enemyY[h] += enemyY_change[h]
            elif enemyX[h] >= 733:
                enemyX_change[h] = -2
                enemyY[h] += enemyY_change[h]

            collision = isCollision(enemyX[h], enemyY[h], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[h] = random.randint(0, 735)
                enemyY[h] = random.randint(50, 150)

            enemy(enemyX[h], enemyY[h], h)

        # Bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        if num_of_enemies == playerImg:
            break

        player(playerX, playerY)
        show_score(textX, textY)

        pygame.display.update()

    pygame.quit()

# Settings menu
def settings_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + volume_step))
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - volume_step))
                elif event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(background, (0, 0))
        title_text = MENU_TITLE_FONT.render("Settings", True, GREEN)
        volume_text = MENU_FONT.render(f"Volume: {int(pygame.mixer.music.get_volume() * 100)}%", True, GREEN)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(volume_text, (WIDTH // 2 - volume_text.get_width() // 2, 250))

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
