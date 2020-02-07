__author__ = "jacksonsr45@gmail.com"

from game import constants as c
from .import*

class Loop(object):
    def loop_game( self, in_game, pg, bg, pos_x, 
                            pos_y, px_snake, py_snake):
        """
        This loop for game 
        While in_game True
        :requere: self.in_game
        :return: self.in_game  
        """
        while in_game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_game = False
                pg.display.update()

            bg.fill(c.WHITE)

            """
            Update and Init class Snake has a snake in game
            """
            Draw_Snake().draw_snake( pg, bg, pos_x, 
                            pos_y, px_snake, py_snake)