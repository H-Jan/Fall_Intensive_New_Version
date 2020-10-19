import sys
import pygame
import pygame.draw

GridSize = width, height = 620, 440
CellSize = 10
SquareDeadColor = 0, 0, 0
SquareAliveColor = 0, 180, 200


class LifeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(GridSize)
        self.clear_screen()
        pygame.display.flip()

        self.init_grids()
        #Initializes the screen
    
    def init_grids(self):
        #num_cols = Width / CellSize
        #num_rows = Height / CellSize
        #Initializes the grids on which our generations will be displayed
        self.game_grid_active = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.game_grid_inactive = [
        ]

     def draw_grid(self):
        #circle_rect = pygame.draw.circle(self.screen, SquareAliveColor, (50, 50), 5, 0)
        pygame.display.flip()


    def clear_screen(self):
        self.screen.fill(SquareDeadColor)
        #Gets rid of previous game display

    def update_generation(self):
        # Inspect current active generation
        # update inactive grid to store next generation
        # swap out the active grid
        pass

 
    def handle_events(self):
        for event in pygame.event.get():
            # if event is keypress of "s" then stop the game
            # if the event is keypress "r" then we will randomize grid
            # if event is keypress of "1" then we will quit
            if event.type == pygame.QUIT:
                sys.exit()


    def run(self):
        #The main game loop, where everything comes together. This is indicative of the 
        # multiple passing generations with Cellular Automata
        while True:
            self.handle_events()
            self.update_generation() #Might need to add time checking with generations so loop isnt quick
            self.draw_grid()


if __name__ == '__main__':
    game = LifeGame()
    game.run()
