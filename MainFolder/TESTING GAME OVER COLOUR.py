import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_COLOR = (0, 0, 0)
BUTTON_TEXT_COLOR = (7, 189, 32)
GAME_OVER_COLOR = (255, 0, 0)  # Set the color to red
BUTTON_FONT = font = pygame.font.SysFont('comicsansms', 70)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME OVER")

# Custom button class
class Button:
    def __init__(self, y, x, width, height, text, action, text_color=BUTTON_TEXT_COLOR):
        self.rect = pygame.Rect(y, x, width, height)
        self.text = text
        self.action = action
        self.clicked = False
        self.text_color = text_color  # Text color for the button

    def draw(self):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        text_surface = BUTTON_FONT.render(self.text, True, self.text_color)  # Use the specified text color
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create buttons
button1 = Button(300, 250, 200, 50, "RESTART GAME", "restart_game")
button2 = Button(300, 400, 200, 50, "Quit", "quit")
button3 = Button(250, 80, 285, 100, "GAME OVER", "game_over", GAME_OVER_COLOR)  # Set the text color to red

buttons = [button1, button2, button3]

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos):
                    if button.action == "restart_game":
                        # Add your start game logic here
                        print("RESTART GAME!")
                    elif button.action == "quit":
                        running = False

    # Draw buttons
    for button in buttons:
        button.draw()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
