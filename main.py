from settings import *
from sys import exit

class Main:
    def __init__(self):
        
        #general
        pygame.init()
        self.display = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # fill screen with grey color
            self.display.fill((grey))
            # Update the game
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":

    main = Main()
    main.run()
    print("Hello World")

# what to include in git ingore for this project
# .vscode
# __pycache__
# *.pyc
# *.pyo
# *.pyd
# how to make git ignore a file
# git rm --cached <file>
# what file?
