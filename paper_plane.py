# example for students from 10th grade comp sci class
# working through Craven's book at programarcadegames.com
# Lab for chapter 8

# design ideas borrowed from student A.M. 

import pygame
import random



pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paper Planez")
 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()





# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,154,23)
RED = (255, 0, 0)
SAGE = (156,175,136)
GRAPE = (128,49,167)
BABY = (155,211,221)
YELLOW = (255,239,0)
BROWN = (101,56,24)
MILLENNIAL = (165,169,160)

tipx = screen_width / 2
tipy = screen_height / 2

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# initial specifications
cloud_num = 8
cloud_list = []
cloud_dims = []
cash_num = 1
cash_list = []
x_num = 4
x_list = []
score = 0
level = 1
# Loops to create randomness

# random position of clouds
for i in range(cloud_num):
    x = random.randrange(0, screen_width)
    y = random.randrange(0, screen_height)
    cloud_list.append([x, y])
# random size of clouds
for i in range(cloud_num):
    width = random.randrange(140, 300)
    height = random.randrange(40, 150)
    cloud_dims.append([width,height])
for i in range(x_num):
    xx = random.randrange(screen_width, screen_width+10)
    xy = random.randrange(0, screen_height)
    x_list.append([xx,xy])
for i in range(x_num):
    xx = random.randrange(screen_width, screen_width+10)
    xy = random.randrange(0, screen_height)
    x_list.append([xx,xy])
for i in range(cash_num):
    cashx = random.randrange(screen_width, screen_width + 20)
    cashy = random.randrange(0,screen_height)
    cash_list.append([cashx,cashy])









# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
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
 
    # User let up on a key
        elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
          elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0
 

 
    # --- Game logic should go here
    # Move the object according to the speed vector.
    tipx += x_speed
    tipy += y_speed 
    # --- Screen-clearing code goes here

    # If you want a background image, replace this clear with blit'ing the background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

  # sun and sky
    pygame.draw.rect(screen, BABY, [0,0,screen_width, screen_height])
    pygame.draw.circle(screen, YELLOW, [300, 20], 30)
  




  
  # clouds
    for i in range(len(cloud_list)):
      pygame.draw.ellipse(screen, WHITE, [cloud_list[i],cloud_dims[i]])
      cloud_list[i][0] -= 1

    # If the cloud has moved off the bottom of the screen
      if cloud_list[i][0] < (0-cloud_dims[i][0]):
        # Reset it just above the top
        y = random.randrange(-10,screen_height)
        cloud_list[i][1] = y
            # Give it a new x position
        x = random.randrange(screen_width, screen_width+20)
        cloud_list[i][0] = x



        # paper airplane
    # let's say the airplane is 80 pixels across
    pygame.draw.polygon(screen, WHITE, 
                        [[tipx,tipy], #1
                        [tipx-50, tipy+80], #2
                        [tipx-66, tipy+50], #3
                        [tipx-75, tipy+66], #4
                        [tipx-63, tipy+63], #5 
                        [tipx-66, tipy+50],   #6  
                        [tipx, tipy], #7
                        [tipx-95, tipy+30],#8
                        [tipx-78, tipy+40],#9
                        [tipx-75, tipy+66], #4 
                        [tipx-66, tipy+50],   #6 
                        [tipx, tipy],#10
                        [tipx-78, tipy+40]#9
                        ]
                       ) 
    pygame.draw.polygon(screen, BLACK, 
                        [[tipx,tipy], #1
                        [tipx-50, tipy+80], #2
                        [tipx-66, tipy+50], #3
                        [tipx-75, tipy+66], #4
                        [tipx-63, tipy+63], #5 
                        [tipx-66, tipy+50],   #6  
                        [tipx, tipy], #7
                        [tipx-95, tipy+30],#8
                        [tipx-78, tipy+40],#9
                        [tipx-75, tipy+66], #4 
                        [tipx-66, tipy+50],   #6 
                        [tipx, tipy],#10
                        [tipx-78, tipy+40]#9
                         
                        ], 
                        width = 3
                       ) 

    # draw cash and exes
    # Select the font to use, size, bold, italics
    # note: replit only allows three fonts: 
    # dejavuserif, dejavusansmono, dejavusans
    font = pygame.font.SysFont('dejavusansmono', 25, True, False)
 
# Render the text. "True" means anti-aliased text.
    for i in range(len(cash_list)): 
      cashes = font.render("$",True,GREEN)
      screen.blit(cashes, [cashx, cashy])
    cashx -= 1
   
    for i in range(len(x_list)):
      exes = font.render("X", True, RED)
      screen.blit(exes, [xx,xy])
    xx -= 1



      # If the X has moved off the bottom of the screen
    if x_list[i][0] < (0):
        # Reset it just above the top
        y = random.randrange(0,screen_height)
        x_list[i][1] = y
            # Give it a new x position
        x = random.randrange(screen_width, screen_width+20)
        x_list[i][0] = x
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
