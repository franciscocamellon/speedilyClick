# -*- coding: utf-8 -*-

import pygame
import random

from src.Square import Random_Square


class Main_Game():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.finish = False
        self.initial_quantity = 20
        self.square_list = []
        

    def init_game(self):
        """ Docstring """
        # Cria relógio
        clock = pygame.time.Clock()

        self.square_list = [Random_Square(self.screen_width, self.screen_height).drawer(self.screen) for i in range(self.initial_quantity)]
        # print(self.square_list)

        self.clocks_counter = 0
        self.second_counter = 0

        self.show_text_time(self.second_counter)

        while not self.finish:

            # Checar os eventos do mouse aqui:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
            
            self.clocks_counter = self.clocks_counter + 1
        
            # A cada 50 conta_clocks, temos 1s (0,02s x 50 = 1s)
            if self.clocks_counter == 50:
                self.second_counter += 1
                self.clocks_counter = 0

            # Limpar tela para atualizar o texto
            self.screen.fill((0,0,0))

            # Já que toda tela foi apagada, desenhar quadradinhos novamente
            for i in self.square_list:
                pygame.draw.rect(self.screen, i[1], i[2])
                # print(i[2])
            # Mostra o tempo atualizado
            self.show_text_time(self.second_counter)

            # Atualiza o desenho na tela
            pygame.display.update()

            # Configura 50 atualizações de tela por segundo
            clock.tick(50)

        # Finaliza a janela do jogo
        pygame.display.quit()
        # Finaliza o pygame
        pygame.quit()
        
    def show_text_time(self, time):
        """ Docstring """
        fonte = pygame.font.Font(None, 24)
        text = fonte.render("Tempo: " + str(time) + "s", 1, (255,255,255))
        textpos = text.get_rect(centerx=self.screen.get_width()/2)
        self.screen.blit(text, textpos)



Main_Game().init_game()