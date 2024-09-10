# main.py

import pygame
import sys

from settings import *
from level import Level

class Game:

    def __init__(self):
        # Set up the game
        pygame.init()
        pygame.display.set_caption('Invaders Of The Corn')

        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
