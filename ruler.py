 



​"""
 Students!
 Use the function `draw_ruler()` to create a ruler grid of pixels on your screen.
 this should give you a good first-approximation of where things should go
 in your drawing. From there, you can make more precise adjustments.

 things to note: the darw ruler function *Requires* that you have variables named
 screen_width and screen_height that match your actual screen width and height. It
 cannot work without them.

 you can just turn on and off the ruler by including the draw_ruler() function in your
 drawing area code or by using a # to comment it out. This allows you to see
 the ruler but also to turn it off easily. 
"""
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)

# Set the height and width of the screen
screen_width = 1000 # this line is essential
screen_height = 700 # so is this line
size = (screen_width, screen_height) #don't say I didn't warn you
def draw_ruler():
    font = pygame.font.SysFont('Calibri', 25, True, False)
    px200 = font.render("200px", True, BLACK)
    px400 = font.render("400px", True, BLACK)
    px600 = font.render("600px", True, BLACK)
    px800 = font.render("800px", True, BLACK)
    screen.blit(px200, [180, 55]) # x axis
    screen.blit(px400, [380, 55])
    screen.blit(px600, [580, 55])
    screen.blit(px800, [780, 55])
    screen.blit(px200, [55, 200]) # y axis
    screen.blit(px400, [55, 400])
    screen.blit(px600, [55, 600])
    screen.blit(px800, [55, 800])
    for x_offset in range(1, screen_width // 50):
        pygame.draw.line(screen, BLACK, [50*x_offset, 0], [50*x_offset, 25], 3)
    for x_offset in range(1, screen_width // 100):
        pygame.draw.line(screen, BLACK, [100*x_offset, 0], [100*x_offset, 50], 5)
    for y_offset in range(1,screen_height//50):
        pygame.draw.line(screen, BLACK, [0, 50*y_offset], [25, 50*y_offset],3)
    for y_offset in range(1,screen_height//100):
        pygame.draw.line(screen, BLACK, [0, 100*y_offset], [50, 100*y_offset],5)    


screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("A ruler for Pixels")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 

    draw_ruler()

 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
