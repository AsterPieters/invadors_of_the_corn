# tools.py

from os import walk
from random import randint
import pygame

from settings import *


def import_folder(path):
    
    list = []

    # Loop through all files
    for folder, sub, files in walk(path):
        
        # Loop through all images
        for image in files:

            # Create the path
            full_path = path + '/' + image
            
            # Put the images in the list
            image_surf = pygame.image.load(full_path).convert_alpha()
            list.append(image_surf)

    return list



def random_coords(sprite_width):
    """ Generate random coordinates """

    # Make sure its in between screen boundaries 
    x_coords = randint(0, SCREEN_WIDTH - sprite_width)
    
    return x_coords



