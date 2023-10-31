import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Variables
WIDTH, HEIGHT = 800, 600
MENU_FONT = pygame.font.SysFont("comicsansms", 75)
MENU_TITLE_FONT = pygame.font.SysFont("comicsansms", 50)
MENU_NAME_FONT = pygame.font.SysFont("comicsansms", 40)
GREEN = (7, 189, 32)
BACKGROUND = pygame.image.load('MainFolder/images/backg.png')
GRAY = (169, 169, 169)

# Create the Pygame window, and name the app at top
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Main Menu")

# Define the main menu options
menu_options = ["Start Game", "Settings", "Exit"]
selected_option = None

# Load and play the soundtrack
pygame.mixer.music.load('MainFolder/sounds/music.mp3')  # Replace with your soundtrack file
pygame.mixer.music.set_volume(0.5)  # Set the initial volume
pygame.mixer.music.play(-1)  # Loop indefinitely

# Volume control
volume_step = 0.1

# The menu titles
def draw_menu():
    screen.blit(BACKGROUND, (0,0))
    title_text = MENU_TITLE_FONT.render("ALIEN INVADERS", True, GREEN)
    title_name = MENU_NAME_FONT.render("By Hamza & Tayyab", True, GREEN)
     
    screen.blit(title_text, (WIDTH // 5 - title_text.get_width() // 100, 17))
    screen.blit(title_name, (WIDTH // 4 - title_name.get_width() // 600, 90))

    for i, option in enumerate(menu_options):
        text = MENU_FONT.render(option, True, GREEN if selected_option == i else GRAY)
        text_rect = text.get_rect(center=(WIDTH // 2, 250 + i * 100))
        screen.blit(text, text_rect)

# Defining main menu and all the buttons
def main_menu():
    global selected_option
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # pygame app will exit if press exit
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
                    # Start the game (replace with game code)
                    print("Starting the game")
                elif selected_option == 1:
                    # Open settings
                    settings_menu()
                elif selected_option == 2:
                    pygame.quit()

        draw_menu()
        pygame.display.flip()

# When you press settings button
def settings_menu():
    global volume
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + volume_step)) # if you press up key turns volume up
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - volume_step)) # if you press down key it turns volume down
                elif event.key == pygame.K_ESCAPE: # When you press escape button it goes back to menu
                    running = False 

        screen.blit(BACKGROUND, (0,0)) #background will stay the same - picture
        title_text = MENU_TITLE_FONT.render("Settings", True, GREEN)
        volume_text = MENU_FONT.render(f"Volume: {int(pygame.mixer.music.get_volume() * 100)}%", True, GREEN)
        
        #places the text in middle of screen
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(volume_text, (WIDTH // 2 - volume_text.get_width() // 2, 250))
        
        #update whole screen
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
