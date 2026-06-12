#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

pygame.init()
window = pygame.display.set_mode((600,480))
print('Setup End')
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #end game