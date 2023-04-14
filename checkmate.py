"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import string
# import random
 
# Define some colors
BLACK = (15, 15, 15)
WHITE = (240, 240, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TAN = (184,134,11)
GRAY = (100, 100, 100)


# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
s_width = 640
s_height = 640
screen = pygame.display.set_mode((s_width, s_height))

square_width = s_width/8
square_height = s_height/8

#TODO: list of 64 coordinate ordered pairs representig locations a1 through h8

sq_names = []
for i in range(1,9):
    for j in list(string.ascii_lowercase[0:8]):
        name = (j,i,)
        sq_names.append(name)
coordinates = []
for i in range(0,8):
    for j in range(0,8):
        coord = (j*square_width+ square_width/2, i*square_height + 1* square_height/2)
        coordinates.append(coord)

def draw_square(screen, x, y):
  pygame.draw.rect(screen, TAN, [x,y, square_width, square_height])

def draw_board(screen):
    for i in range(0,8):
      if i % 2 == 0:
        for j in range(0,7,2):
          draw_square(screen, square_width*j, square_height*i)
      else:  
        for j in range(1,9,2):
          draw_square(screen, square_width*j, square_height*i)

def draw_pawn(screen, color, x, y):
  pygame.draw.rect(screen, color, [x-15, y-5, 30, 5])
  pygame.draw.rect(screen, BLACK, [x-15, y-5, 30, 5],2)
  pygame.draw.polygon(screen, color, [(x+5, y-10), (x+15, y+30), (x-15, y+30), (x-5, y-10)], 0)
  pygame.draw.rect(screen, color, [x-20, y+30, 40, 7])
  pygame.draw.polygon(screen, BLACK, [(x+5, y-10), (x+15, y+30), (x-15, y+30), (x-5, y-10)], 2)
  pygame.draw.rect(screen, BLACK, [x-20, y+30, 40, 7],2)
  pygame.draw.circle(screen, color, [x,y-(square_height/4)], 18)
  pygame.draw.circle(screen, BLACK, [x,y-(square_height/4)], 18, 2)


pygame.display.set_caption("Checkmate. ")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
x_speed_2 = 0
y_speed_2 = 0
  
# Current position
x_coord = coordinates[0][0]
y_coord = coordinates[0][1]
x_coord_2 = coordinates[56][0]
y_coord_2 = coordinates[56][1]
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_a:
                x_speed_2 = -3
            elif event.key == pygame.K_d:
                x_speed_2 = 3
            elif event.key == pygame.K_w:
                y_speed_2 = -3
            elif event.key == pygame.K_s:
                y_speed_2 = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed_2 = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed_2 = 0
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    y_coord_2 = y_coord_2 + y_speed_2
    x_coord_2 = x_coord_2 + x_speed_2
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    draw_board(screen)
    draw_pawn(screen, WHITE, x_coord, y_coord)
    draw_pawn(screen, GRAY, x_coord_2, y_coord_2)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
