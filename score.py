from settings import *

# create a class for the score
class Score:

    # init function to initialize the score
    def __init__(self):

        # set the surface
        self.surface = pygame.Surface((sidebar_width,score_height_fraction * game_height))
        
        # set the display surface
        self.display_surface = pygame.display.get_surface()

    # function to run the score
    def run(self):

        # draw the surface
        self.display_surface.blit(self.surface, (game_width + 2 * padding, padding + preview_height_fraction * game_height))

       
