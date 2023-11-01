import pygame
import sys

# Initialize Pygame
pygame.init()


# Variables
WIDTH, HEIGHT = 800, 600
OPTIONS_FONT = pygame.font.SysFont("comicsansms", 65)
MENU_CONGRAT_FONT = pygame.font.SysFont("comicsansms", 35)
GREEN = (7, 189, 32)
BACKGROUND = pygame.image.load('MainFolder/images/backg.png')
GRAY = (169, 169, 169)

# Create the Pygame window, and name the app at top
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ALIEN INVADERS")

# Define the main menu options
menu_options = ["CLICK FOR LEVEL 2", "Exit"]
selected_option = None

# The menu titles
def main_menu(): 
screen.blit(BACKGROUND, (0,0))
congrat_text = MENU_CONGRAT_FONT.render("CONGRATULATIONS! LEVEL 1 COMPLETE", True, GREEN)
     
screen.blit(congrat_text, (WIDTH // 15 - congrat_text.get_width() // 100, 17))

for i, option in enumerate(menu_options):
        text = OPTIONS_FONT.render(option, True, GREEN if selected_option == i else GRAY)
        text_rect = text.get_rect(center=(WIDTH // 2, 250 + i * 100))
        screen.blit(text, text_rect)

# Defining main menu and all the buttons
def opt_menu():
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
                    text_rect = OPTIONS_FONT.render(option, True, GREEN).get_rect(center=(WIDTH // 2, 300 + i * 60))
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        selected_option = i
                        break
                else:
                    selected_option = None
            if event.type == pygame.MOUSEBUTTONDOWN and selected_option is not None:
                if selected_option == 0:
                    print("Starting LEVEL 2")
                elif selected_option == 1:
                    pygame.quit()

        main_menu()
        pygame.display.flip()

        
if __name__ == "__main__":
    main_menu()
