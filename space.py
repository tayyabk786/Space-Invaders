import pygame

pygame.init()

#CREATE THE GAME WINDOW
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#define the fonts
font = pygame.font.SysFont("comicsansms", 50)
font2 = pygame.font.SysFont("comicsansms", 32)


#define the colour of the text
TEXT_COL = (7, 189, 32)

def draw_text2(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))




    
#GAME LOOP
run = True
while run: 
    screen.fill((52, 78, 91))

    #print the text in the desired font, colour and location on screen 
    draw_text("SPACE INVADERS", font, TEXT_COL, 190, 250)
    draw_text2("BY HAMZA AND TAYYAB", font2, TEXT_COL, 200, 320)




    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit