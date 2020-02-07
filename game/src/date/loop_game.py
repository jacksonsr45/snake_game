__author__ = "jacksonsr45@gmail.com"

from game import constants as c
from .import*

class Loop(object):
    def loop_game( self, in_game, pg, bg, pos_x, 
                            pos_y, px_snake, py_snake, 
                            p_snake, speed_x, speed_y, fps):
        """
        This loop for game 
        While in_game True
        :requere: self.in_game
        :return: self.in_game  
        """
        while in_game:
            """
            Limit for FPS in game 
            """
            fps.tick(15)
            """
            Booting EVENTS in game 
            """
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    in_game = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        speed_y = 0
                        speed_x = -p_snake
                    if event.key == pg.K_RIGHT:
                        speed_y = 0
                        speed_x = p_snake
                    if event.key == pg.K_UP:
                        speed_x = 0
                        speed_y = -p_snake
                    if event.key == pg.K_DOWN:
                        speed_x = 0
                        speed_y = p_snake
            
            """
            Init screen back gound with color 
            WHITE from game and update in loop
            """
            bg.fill(c.WHITE)
            
            """
            int pos_x and pos_y the snake with 
            speed_x and speed_y
            """                              
            pos_x += speed_x
            pos_y += speed_y

            """
            Display Updade <- fps in looping
            """
            pg.display.update()
            

            """
            Update and Init class Snake has a 
            snake in game
            """
            Draw_Snake().draw_snake( pg, bg, pos_x, 
                            pos_y, px_snake, py_snake)