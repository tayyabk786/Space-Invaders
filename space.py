import pygame

pygame.init()

#CREATE THE GAME WINDOW
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#define the fonts
font = pygame.font.SysFont("comicsansms", 50)
font2 = pygame.font.SysFont("comicsansms", 30)


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
    draw_text("ALIEN INVADERS", font, TEXT_COL, 160, 5)
    draw_text2("BY HAMZA AND TAYYAB", font2, TEXT_COL, 200, 70)




    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    # defining button, initialising its properties
class Button():
    def _init_(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
#update screen puts its image and text on screen
def update(self, screen):
    if self.image is not None:
        screen.blit(self.image, self.rect)
    screen.blit(self.text, self.text_rect)
#check for input checks if we are clicking on the button
def checkforInput(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        return True
    return False
#change color is for if mouse is hovering over button it will change to desired colour
def changeColor(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        self.text = self.font.render(self.text_input, True, self.hovering_color)
    else:
        self.text = self.font.render(self.text_input, True, self.base_color)

pygame.quit