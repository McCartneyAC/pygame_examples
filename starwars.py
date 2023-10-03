import pygame, sys
import random
import time
from itertools import product
from pygame.locals import QUIT
clock = pygame.time.Clock()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,0, 255)
LIGHTBLUE = (80, 220, 220)
width, height = 1000, 700
pygame.font.init()
#available = pygame.font.get_fonts()
font = pygame.font.SysFont("dejavusans", 25, True, False)

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Professor McCartney's silly game")
done = False
k = 0

## Star coordinates
coordinates = [(x, y) for x in range(width) for y in range(height)]
coordinates = random.sample(coordinates, 200)
for i in range (3):
  text = font.render("A long time ago in a galaxy far, far away...",True,LIGHTBLUE)
  screen.blit(text, [50, 50])
  
  time.sleep(1)
  pygame.display.flip()
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          print("User pressed a key.")
        elif event.type == pygame.KEYUP:
          print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print("User pressed a mouse button")
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    for i in range(len(coordinates)):
      pygame.draw.circle(screen, WHITE, coordinates[i], random.randrange(1,3))


    # Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
    renderTextCenteredAt("It is a period of civil wars in the galaxy. A brave alliance of underground freedom fighters has challenged the tyranny and oppression of the awesome GALACTIC EMPIRE. \n Striking from a fortress hidden among the billion stars of the galaxy, rebel spaceships have won their first victory in a battle with the powerful Imperial Starfleet. The EMPIRE fears that another defeat could bring a thousand more solar systems into the rebellion, and Imperial control over the galaxy would be lost forever. \n To crush the rebellion once and for all, the EMPIRE is constructing a sinister new battle station. Powerful enough to destroy an entire planet, its completion spells certain doom for the champions of freedom.",font, YELLOW, (width / 2), (height -100)+k, screen, (width-100))

# Put the image of the text on the screen at 250x250
    screen.blit(text, [10, 400+k])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(30)
    k -= 1
   
# Close the window and quit.
pygame.quit()
