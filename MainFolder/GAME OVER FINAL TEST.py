import pygame

pygame.init()
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
obstacle_x = 400
obstacle_y = 400
obstacle_width = 40
obstacle_height = 40
player_x = 200
player_y = 400
player_width = 20
player_height = 20
game_state = "start_menu"

#background

background = pygame.image.load('images/image.png')

def draw_start_menu():
   #screen.fill((52, 78, 91))
   screen.blit(background, (0,0))
   font = pygame.font.SysFont('comicsansms', 70)
   title = font.render('GAME OVER', True, (255,48,48))
   quit_button = font.render('PRESS Q TO QUIT', True, (7, 189, 32))
   start_button = font.render('PRESS R TO RESTART', True, (7, 189, 32))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/10 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/5 + start_button.get_height()/2))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()

def draw_game_over_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()
   if game_state == "start_menu":
       draw_start_menu()
       keys = pygame.key.get_pressed()

