from settings import *

class Preview:

    def __init__(self):

        # set the surface
        self.surface = pygame.Surface(
            (sidebar_width, preview_height_fraction * game_height))

        # set the display surface
        self.display_surface = pygame.display.get_surface()

    def run(self):

        # draw the surface
        self.display_surface.blit(
            self.surface, (game_width + 2 * padding, padding))

        # change the color of the surface
        self.surface.fill((red))