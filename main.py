#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'inory'

import pygame
from pygame.locals import *
from sys import *

screen_size = (800, 600)

pygame.init()

# Create a window
screen = pygame.display.set_mode(
    screen_size, 0, 32)
# Set the window title
pygame.display.set_caption('My RPG')

screen.fill((0,0,0))

# Main loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Refresh the screen
    pygame.display.update()