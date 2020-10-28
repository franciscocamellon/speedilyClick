# -*- coding: utf-8 -*-

import pygame
import random

from src.Square import Random_Square
from src.Time import Show_Time as time
from src.Punctuation import Show_Points as points

class Main_Game():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.init()
        pygame.display.set_caption('Speedily Click - from Francisco Camello')
        pygame.mixer.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.finish = False
        self.initial_quantity = 20
        self.square_list = []
        self.initial_time = 10
        

    def init_game(self):
        """ Docstring """
        # Cria relógio
        clock = pygame.time.Clock()

        self.square_list = [Random_Square(self.screen_width, self.screen_height).drawer(self.screen) for i in range(self.initial_quantity)]
        # print(self.square_list)

        self.clocks_counter = 0
        self.second_counter = self.initial_time
        self.points = 0

        # efeito = pygame.mixer.Sound('click.wav')

        # self.show_text_time(self.second_counter)

        while not self.finish:

            # Checar os eventos do mouse aqui:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_position = pygame.mouse.get_pos()

                    for i in self.square_list:
                        if i[2].collidepoint(click_position):
                            self.square_list.remove(i)
                            self.points += 1


                if event.type == pygame.QUIT:
                    self.finish = True
            
            self.clocks_counter = self.clocks_counter + 1
        
            # A cada 50 conta_clocks, temos 1s (0,02s x 50 = 1s)
            if self.clocks_counter == 50:
                if self.second_counter >= 0:
                    self.second_counter -= 1
                self.clocks_counter = 0

                new_sq = Random_Square(self.screen_width, self.screen_height).drawer(self.screen)
                self.square_list.append(new_sq)
                # print(self.square_list)

            if self.second_counter >= 0:
                # Limpar tela para atualizar o texto
                self.screen.fill((0,0,0))

                # Já que toda tela foi apagada, desenhar quadradinhos novamente
                for i in self.square_list:
                    pygame.draw.rect(self.screen, i[1], i[2])
                    # print(i[2])
                # Mostra o tempo atualizado
                time().show_text_time(self.screen, self.second_counter, self.points)
            else:
                points().show_final_points(self.screen, self.points)

            # Atualiza o desenho na tela 
            pygame.display.update()

            # Configura 50 atualizações de tela por segundo
            clock.tick(50)

        # Finaliza a janela do jogo
        pygame.display.quit()
        # Finaliza o pygame
        pygame.quit()
        
    



Main_Game().init_game()