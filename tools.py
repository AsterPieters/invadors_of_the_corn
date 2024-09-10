# tools.py

from os import walk
import pygame


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

