import sys
import pygame
import pygame.draw

GridSize = width, height = 620, 440
SquareDeadColor = 0, 0, 0
SquareAliveColor = 0, 180, 200

class LifeGame: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(GridSize)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(SquareDeadColor)


            pygame.display.flip()


if __name__= '__main__':
    game = LifeGame()
    game.run()

