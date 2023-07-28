from settings import *

# create a class for the main game
class Game:

    # init function to initialize the game
    def __init__(self):

        #           GENERAL
        # set the surface
        self.surface = pygame.Surface((game_width,game_height))
        
        # set the display surface   
        self.display_surface = pygame.display.get_surface()

        # add reactangle to the surface
        self.rect = self.surface.get_rect(topleft = (padding,padding))

        #           BLOCKS
        # create a group for the blocks
        self.blocks = pygame.sprite.Group()

        #

        #           LINES
        # line surface with default black color
        self.line_surface = self.surface.copy()

        # fill line surface with yellow color
        self.line_surface.fill((yellow))

        # set the color key not used anywhere
        self.line_surface.set_colorkey((yellow))

        # alpha value which is used for tranparency
        # on line surface
        # 0 means fully transparent
        # 255 means fully opaque
        self.line_surface.set_alpha(100)

        # test block
        self.block = Block(self.blocks, pygame.Vector2(1,1),yellow)
       


    # function to draw the grid on top of game surface
    def draw_grid(self):

        # loop through the columns
        for col in range(1,columns):

            # calculate the x coordinate
            x = col * cell_size

            # draw the line
            pygame.draw.line(self.line_surface,line_color,
                             (x,0),(x,self.surface.get_height()),1)
            
        # loop through the rows
        for row in range(1,rows):
                
                # calculate the y coordinate
                y = row * cell_size
    
                # draw the line
                pygame.draw.line(self.line_surface,line_color,
                                (0,y),(self.surface.get_width(),y),1)
                
        # draw the line surface on the game surface
        self.surface.blit(self.line_surface,(0,0))

        

    # function to run the game
    def run(self):

        # draw the grid
        self.draw_grid()

        # draw blocks
        self.blocks.draw(self.surface)

        # draw the surface
        # add padding at lower end
        self.display_surface.blit(self.surface, (padding,padding))

        # change the color of the surface
        self.surface.fill((grey))

        # draw the rectangle
        pygame.draw.rect(self.display_surface,line_color,self.rect,1,1)

# create a class for the blocks
class Block(pygame.sprite.Sprite):
     
    # init function to initialize the block
     def __init__(self, blocks, position, color):

        # call the parent class constructor
        super().__init__(blocks)

        # set the image
        self.image = pygame.Surface((cell_size,cell_size))

        # fill the image with yellow color
        self.image.fill((color))

        # position of the block
        self.position = position
        x = position.x * cell_size
        y = position.y * cell_size


        # draw the rectangle
        self.rect = self.image.get_rect(topleft = (x,y))


class Tetromino:
     def __init__(self,shape,group):
          self.block_positions = []