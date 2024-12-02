# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MARKER_RED = (173,72,72)
EMERALD = (53,137,119)
SKY = (31,133,222)
BRICK = (222,120,31)
GREY = (240,240,240)
PURPLE = (111,45,168)


PIXEL_X = 16
PIXEL_Y = 16
MARGIN = 4

grid2= []
 # new plan
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,1,5,5,0,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,5,5,5,5,1,1,1,5,1,5,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,5,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,5,0,0,0,0]
grid2.append(row)
row = [0,0,0,5,5,0,0,0,0,0,0,0,0,1,1,1,1,1,1,5,5,1,1,1,1,1,1,1,1,5,5,0,0,0,0]
grid2.append(row)
row = [0,0,2,2,2,5,5,0,5,5,5,5,5,5,5,5,5,5,5,2,2,5,1,1,1,1,1,1,1,5,1,5,0,0,0]
grid2.append(row)
row = [0,0,2,2,2,2,5,5,2,2,2,2,2,2,2,2,5,2,2,2,2,5,1,1,1,1,1,1,1,5,1,1,5,0,0]
grid2.append(row)
row = [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,1,1,1,1,1,1,1,1,5,1,5,0,0]
grid2.append(row)
row = [0,0,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,1,1,1,1,1,1,1,5,1,1,5,0]
grid2.append(row)
row = [0,0,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,1,1,1,1,1,1,1,1,5,1,5,0]
grid2.append(row)
row = [0,0,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,1,1,1,1,1,1,1,1,5,1,1,5]
grid2.append(row)
row = [0,5,5,2,2,2,2,2,2,2,2,2,2,2,2,5,4,4,5,2,2,2,2,5,1,1,1,1,1,1,1,5,1,1,5]
grid2.append(row)
row = [0,5,3,2,2,2,2,2,2,2,2,2,2,2,5,3,3,0,4,5,2,2,2,5,5,1,1,1,1,1,1,5,1,1,5]
grid2.append(row)
row = [0,5,3,2,2,2,2,2,2,2,2,2,2,2,5,3,3,0,0,5,2,2,2,5,5,1,1,1,1,1,5,1,1,1,5]
grid2.append(row)
row = [5,4,3,0,2,2,2,2,2,2,2,2,2,2,3,0,3,3,0,4,2,2,2,5,2,5,1,1,1,1,5,1,1,1,5]
grid2.append(row)
row = [5,0,3,0,2,2,2,2,2,2,2,2,2,2,3,0,3,3,0,4,2,2,2,5,2,2,5,1,1,5,1,1,1,5,0]
grid2.append(row)
row = [5,2,3,3,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,2,2,2,2,2,2,2,2,5,5,1,1,1,1,5,0]
grid2.append(row)
row = [5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,5,1,1,5,0,0]
grid2.append(row)
row = [5,2,5,5,2,2,2,2,2,5,2,2,2,2,2,2,5,5,5,5,2,2,5,2,2,2,5,5,2,2,5,5,0,0,0]
grid2.append(row)
row = [0,5,2,0,3,3,2,2,2,2,2,5,5,5,5,5,0,5,2,2,2,2,5,2,2,2,5,5,5,2,2,5,0,0,0]
grid2.append(row)
row = [0,0,5,2,2,5,3,3,3,3,3,3,3,3,3,3,5,2,2,2,2,5,2,2,2,2,2,5,5,2,2,2,5,0,0]
grid2.append(row)
row = [0,0,0,5,5,2,2,5,3,3,3,3,3,3,5,2,2,2,2,5,5,2,2,2,2,2,5,2,2,2,2,2,5,0,0]
grid2.append(row)
row = [0,0,0,0,0,5,5,2,2,2,2,2,2,2,2,2,5,5,5,2,2,2,5,2,2,5,2,2,2,5,2,2,2,5,0]
grid2.append(row)
row = [0,0,0,0,0,5,2,5,5,5,5,5,5,5,5,5,2,2,2,2,2,2,5,2,2,5,2,2,5,5,5,2,2,5,0]
grid2.append(row)
row = [0,0,0,0,0,2,2,2,2,2,5,2,2,2,2,2,2,5,2,2,2,2,2,5,5,2,2,2,5,5,5,2,2,5,0]
grid2.append(row)
row = [0,0,0,0,0,0,5,2,2,2,2,5,5,2,2,2,5,2,2,2,2,2,2,5,5,2,2,2,5,5,5,2,2,5,0]
grid2.append(row)
row = [0,0,0,0,0,0,5,2,2,2,2,2,2,5,5,5,5,2,2,2,2,2,2,5,5,2,2,2,2,5,2,2,5,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,2,2,2,2,2,2,2,5,0,0,2,2,2,2,2,2,2,5,0,5,5,2,5,2,5,2,5,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,5,2,2,2,2,2,5,0,0,2,2,2,2,2,2,5,0,0,5,0,5,0,5,0,5,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,5,0,5,0,5,2,5,0,0,0,5,2,2,2,2,2,5,0,0,0,5,5,5,5,5,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,5,5,5,5,5,0,0,0,5,0,5,0,5,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0]
grid2.append(row)
row = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
grid2.append(row)


print(grid2)

# Set the height and width of the screen
size = (744, 744)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bulbasoaring to New Heights")
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    # Clear the screen and set the screen background
    screen.fill(WHITE)


# drawing code here
    for row in range(32):
        for column in range(32):
            color = GREY
            if grid2[row][column] == 1:
                color = EMERALD
            elif grid2[row][column]==2:
                color = SKY
            elif grid2[row][column]==3:
                color =  MARKER_RED
            elif grid2[row][column]==4:
                color = BRICK
            elif grid2[row][column]==5:
                color = BLACK
            pygame.draw.rect(screen, color, [(MARGIN + PIXEL_X) * column + MARGIN, # x
                                                (MARGIN + PIXEL_Y) * row + MARGIN,
                              PIXEL_X,
                              PIXEL_Y])
    pygame.display.flip()
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
# Be IDLE friendly
pygame.quit()