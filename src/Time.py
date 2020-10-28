# -*- coding: utf-8 -*-

import pygame


class Show_Time():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        self.text = ''
        self.color = (255,255,255)


    def show_text_time(self, screen, time, points):
        """ Docstring """

        self.text = self.font.render("Tempo: " + str(time) + "s | Pontuação: " + str(points), 1, (255,255,255))
        textpos = self.text.get_rect(centerx=screen.get_width()/2)
        screen.blit(self.text, textpos)