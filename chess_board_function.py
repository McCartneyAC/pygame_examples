# front matter:
s_width = 640
s_height = 640
# screen = pygame.display.set_mode((s_width, s_height))

square_width = s_width/8
square_height = s_height/8

# square function
def draw_square(screen, x, y):
  pygame.draw.rect(screen, TAN, [x,y, square_width, square_height])

  
# version one, long and foolish:
def draw_board(screen):
    draw_square(screen, 0,0)
    draw_square(screen, square_width*2, 0)
    draw_square(screen, square_width*4, 0)
    draw_square(screen, square_width*6, 0)
    draw_square(screen, square_width, square_height)
    draw_square(screen, square_width*3, square_height)
    draw_square(screen, square_width*5, square_height)
    draw_square(screen, square_width*7, square_height)
    draw_square(screen, 0,square_height*2)
    draw_square(screen, square_width*2, square_height*2)
    draw_square(screen, square_width*4, square_height*2)
    draw_square(screen, square_width*6, square_height*2)
    draw_square(screen, square_width, square_height*3)
    draw_square(screen, square_width*3, square_height*3)
    draw_square(screen, square_width*5, square_height*3)
    draw_square(screen, square_width*7, square_height*3)
    draw_square(screen, 0,square_height*4)
    draw_square(screen, square_width*2, square_height*4)
    draw_square(screen, square_width*4, square_height*4)
    draw_square(screen, square_width*6, square_height*4)
    draw_square(screen, square_width, square_height*5)
    draw_square(screen, square_width*3, square_height*5)
    draw_square(screen, square_width*5, square_height*5)
    draw_square(screen, square_width*7, square_height*5)
    draw_square(screen, 0,square_height*6)
    draw_square(screen, square_width*2, square_height*6)
    draw_square(screen, square_width*4, square_height*6)
    draw_square(screen, square_width*6, square_height*6)
    draw_square(screen, square_width, square_height*7)
    draw_square(screen, square_width*3, square_height*7)
    draw_square(screen, square_width*5, square_height*7)
    draw_square(screen, square_width*7, square_height*7)
    
    
    # version two: getting compact:
    def draw_board(screen):
    for i in [0,2,4,6]:
      draw_square(screen, square_width*i, 0)
    for i in [1,3,5,7]:
      draw_square(screen, square_width*i, square_height)
    for i in [0,2,4,6]:
      draw_square(screen, square_width*i, square_height*2)
    for i in [1,3,5,7]:
      draw_square(screen, square_width*i, square_height*3)
    for i in [0,2,4,6]:
      draw_square(screen, square_width*i, square_height*4)
    for i in [1,3,5,7]:
      draw_square(screen, square_width*i, square_height*5)
    for i in [0,2,4,6]:
      draw_square(screen, square_width*i, square_height*6)
    for i in [1,3,5,7]:
      draw_square(screen, square_width*i, square_height*7)


# version three: doing it with real python
def draw_board(screen):
    for i in range(0,7):
      if i % 2 == 0:
        for j in range(0,7,2):
          draw_square(screen, square_width*j, square_height*i)
      else:  
        for j in range(1,9,2):
          draw_square(screen, square_width*j, square_height*i)
