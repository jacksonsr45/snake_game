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
                        """
                        Direction == LEFT
                        """ 
                        speed_y = 0
                        speed_x = -p_snake
                    if event.key == pg.K_RIGHT:
                        """
                        Direction == RIGHT
                        """ 
                        speed_y = 0
                        speed_x = p_snake
                    if event.key == pg.K_UP:
                        """
                        Direction == UP
                        """ 
                        speed_x = 0
                        speed_y = -p_snake
                    if event.key == pg.K_DOWN:
                        """
                        Direction == DOWN
                        """ 
                        speed_x = 0
                        speed_y = p_snake
                    if event.key == pg.K_ESCAPE:
                        """
                        Press ESC to scape the game 
                        :in_game: return False to escape game
                        """ 
                        in_game = False
                    if event.key == pg.K_SPACE:
                        """
                        pause speed to the game 
                        or pause game
                        """ 
                        speed_x = 0
                        speed_y = 0
            
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
            Update and Init class Snake has a 
            snake in game
            """
            snake = Draw_Snake().draw_snake( pg, bg, pos_x, 
                                        pos_y, px_snake, py_snake)


            """
            Testind colision with board screen 
            """
            if pos_x > c.WIDTH-10:#Right
                pos_x -= 10
                speed_x = 0
                speed_y = 0
            elif pos_x < 0:#left
                pos_x = 0
                speed_x = 0
                speed_y = 0
            elif pos_y > c.HEIGHT-10:#down
                pos_y -= 10
                speed_x = 0
                speed_y = 0
            elif pos_y < 0:#up
                pos_y = 0
                speed_x = 0
                speed_y = 0
            
            """
            Display Updade <- fps in looping
            """
            pg.display.update()