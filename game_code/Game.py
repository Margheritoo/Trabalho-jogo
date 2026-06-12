#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from game_code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((600, 480))

def run(self):
    while True:
        menu = Menu(self.window)
        menu.run()
        pass

    # Check for events
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        pygame.quit() #Close window
    #        quit() #end game