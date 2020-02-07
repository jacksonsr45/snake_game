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
        Init Values default for Snake
        :p_snake: This is value in pixels for snake
        :pos_x: This is pos in X in screen  
        :pos_y: This is pos in Y in screen
        """
        self.speed_x = 0
        self.speed_y = 0
        self.p_snake = 10
        self.pos_x = randint(0, (c.WIDTH - self.p_snake)/10)*10
        self.pos_y = randint(0, (c.HEIGHT - self.p_snake)/10)*10

        """
        Init self.in_game with True 
        While is true in game else out game
        """
        self.in_game = True
        
        """
        This is a loop in data/loop_game.py
        """
        Loop().loop_game(self.in_game, self.pg, self.back_ground, 
                        self.pos_x, self.pos_y, self.p_snake, 
                        self.p_snake, self.p_snake, self.speed_x, 
                        self.speed_y, self.fps)           