__author__ = "jacksonsr45@gmail.com"

from game import constants as c
from .import*


class Snake:
    def __init__(self, pygame):
        """
        This is main to the game
        :pygame: pygame init in main
        """
        self.pg = pygame
        self.back_ground = self.pg.display.set_mode([c.WIDTH,c.HEIGHT])
        self.pg.display.set_caption("Snake the GAME")
        """
        Atribute for FPS in loop game
        """
        self.fps = self.pg.time.Clock()
        

        """
        Init self.in_game with True 
        While is true in game else out game
        """
        self.in_game = True
        
        """
        This is a loop in data/loop_game.py
        """
        Loop().loop_game(self.in_game, self.pg, self.back_ground,
                            self.fps)           