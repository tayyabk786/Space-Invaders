import pygame

#line 3 is used to Intialize the pygame
pygame.init()

#line 7- we are created the screen for the game 
screen = pygame.display.set_mode((800, 600))

# Titile andIcon of the game
pygame.display.set_caption("Alien Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

#Game loop and event handler 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Line 23 is setting the color of the game and 24 shows the color
    screen.fill((32, 32, 32))
    
    player()
    pygame.display.update()