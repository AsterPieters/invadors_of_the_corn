# Settings.py

import pygame

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colours
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

LAYERS = {
	'sky': 0,
	'ground': 1,
}
