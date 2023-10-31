import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
MENU_FONT = pygame.font.SysFont("comicsansms", 75)
MENU_TITLE_FONT = pygame.font.SysFont("comicsansms", 50)
MENU_NAME_FONT = pygame.font.SysFont("comicsansms", 40)
GREEN = (7, 189, 32)
BACKGROUND = pygame.image.load('MainFolder/images/backg.png')
GRAY = (169, 169, 169)
