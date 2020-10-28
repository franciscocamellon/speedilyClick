# -*- coding: utf-8 -*-

import pygame


class Show_Points():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.text = ''
        self.color = (0,0,0)


    def show_final_points(self, screen, points):
        """ Docstring """

        screen.fill(self.color) # Limpa tela
        self.text = self.font.render("Pontuação: " + str(points) + " quadradinhos", 1, (255,255,255))
        textpos = self.text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(self.text, textpos)
