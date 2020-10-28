# -*- coding: utf-8 -*-

import pygame
import random


class Random_Square():
    """ Docstring """

    def __init__(self, screen_width, screen_height):
        """ Constructor """
        self.width = 30
        self.height = 30
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)
        self.area = pygame.Rect(self.x, self.y, self.height, self.width)
        self.color = (random.randint(20, 255), random.randint(
            20, 255), random.randint(20, 255))

    def drawer(self, screen):
        """ Docstring """
        sq = pygame.draw.rect(screen, self.color, self.area)
        return sq, self.color, self.area
