from settings import *

# create a class for the main game
class Game:

    # init function to initialize the game
    def __init__(self):

        # set the surface
        self.surface = pygame.Surface((game_width,game_height))
        
        # set the display surface   
        self.display_surface = pygame.display.get_surface()

    # function to run the game
    def run(self):

        # draw the surface
        # add padding at lower end
    
        self.display_surface.blit(self.surface, (padding,padding))
