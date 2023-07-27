from settings import *

# create a class for the main game
class Game:

    # init function to initialize the game
    def __init__(self):

        # set the surface
        self.surface = pygame.Surface((game_width,game_height))
        
        # set the display surface   
        self.display_surface = pygame.display.get_surface()


    # function to draw the grid on top of game surface
    def draw_grid(self):

        # loop through the columns
        for col in range(1,columns):

            # calculate the x coordinate
            x = col * cell_size

            # draw the line
            pygame.draw.line(self.surface,line_color,
                             (x,0),(x,self.surface.get_height()),1)

    # function to run the game
    def run(self):

        # draw the grid
        self.draw_grid()

        # draw the surface
        # add padding at lower end
    
        self.display_surface.blit(self.surface, (padding,padding))
        # change the color of the surface
        self.surface.fill((white))