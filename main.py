from settings import *
from sys import exit

# create a class for the main game
class Main:
    # initialize the game
    def __init__(self):
        
        #general
        pygame.init()
        # set the display window
        self.display = pygame.display.set_mode((640,480))
        # set the clock
        self.clock = pygame.time.Clock()
        # set the title of the window
        pygame.display.set_caption("Tetris")
    
    # function run the game
    def run(self):
        # game loop
        while True:
            # check for events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # quit the game
                    pygame.quit()
                    # exit the program
                    exit()
            # fill screen with grey color
            self.display.fill((grey))
            # Update the game
            pygame.display.update()
            # set the fps
            self.clock.tick(60)

# run the game
if __name__ == "__main__":
    # Create the game object
    main = Main()
    # Run the game
    main.run()


