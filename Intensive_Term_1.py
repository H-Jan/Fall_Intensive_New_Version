import sys, pygame
import pygame.draw

GridSize = width, height = 620, 440
SquareDeadColor = 0, 0, 0
SquareAliveColor = 0, 180, 200


pygame.init()
screen = pygame.display.set_mode(GridSize)

circle_rect = pygame.draw.circle(screen, SquareAliveColor, (50, 50), 5, 0)
print(type(circle_rect))
print(circle_rect)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(SquareDeadColor)


