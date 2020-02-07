__author__ = "jacksonsr45@gmail.com"

from game import constants as c
from .import*

class Loop(object):
    def loop_game( self, in_game, pg, bg, fps):
        """
        This loop for game 
        While in_game True
        :requere: self.in_game
        :return: self.in_game  
        """
        
        self.snake_cont = []
        cont = 0
        self.snake_x = randint(0, (c.WIDTH - c.PX)/10)*10
        self.snake_y = randint(0, (c.HEIGHT - c.PX)/10)*10
        self.apple_x = randint(0, (c.WIDTH - c.PX)/10)*10
        self.apple_y = randint(0, (c.HEIGHT - c.PX)/10)*10
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
                    if event.key == pg.K_LEFT and c.SPEED_X != c.PX:
                        """
                        Direction == LEFT
                        """ 
                        c.SPEED_Y = 0
                        c.SPEED_X = -c.PX
                    if event.key == pg.K_RIGHT and c.SPEED_X != -c.PX:
                        """
                        Direction == RIGHT
                        """ 
                        c.SPEED_Y = 0
                        c.SPEED_X = c.PX
                    if event.key == pg.K_UP and c.SPEED_Y != c.PX:
                        """
                        Direction == UP
                        """ 
                        c.SPEED_X = 0
                        c.SPEED_Y = -c.PX
                    if event.key == pg.K_DOWN and c.SPEED_Y != -c.PX:
                        """
                        Direction == DOWN
                        """ 
                        c.SPEED_X = 0
                        c.SPEED_Y = c.PX
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
                        c.SPEED_X = 0
                        c.SPEED_Y = 0
            
            """
            Init screen back gound with color 
            WHITE from game and update in loop
            """
            bg.fill(c.WHITE)
            
            """
            int pos_x and pos_y the snake with 
            speed_x and speed_y
            """                              
            self.snake_x += c.SPEED_X
            self.snake_y += c.SPEED_Y

            
            """
            Update and Init class Apple            """
            Draw_Apple().__apple__( pg, bg, self.apple_x,
                                    self.apple_y, c.PX, c.PX)
            
            """
            Update and Init class Snake
            """
            self.__snake_init = []
            self.__snake_init.append(self.snake_x)
            self.__snake_init.append(self.snake_y) 
            self.snake_cont.append(self.__snake_init)
            Draw_Snake().draw_snake( pg, bg, self.snake_cont, c.PX, c.PX)

            if len(self.snake_cont) > cont:
                del self.snake_cont[0]

            if self.snake_x == self.apple_x and self.snake_y == self.apple_y:
                self.apple_x = randint(0, (c.WIDTH - c.PX)/10)*10
                self.apple_y = randint(0, (c.HEIGHT - c.PX)/10)*10
                cont += 1

            """
            Testind colision with board screen 
            """
            if self.snake_x > c.WIDTH-10:#Right
                self.snake_x -= 10
                c.SPEED_X = 0
                c.SPEED_Y = 0
            elif self.snake_x < 0:#left
                self.snake_x = 0
                c.SPEED_X = 0
                c.SPEED_Y = 0
            elif self.snake_y > c.HEIGHT-10:#down
                self.snake_y -= 10
                c.SPEED_X = 0
                c.SPEED_Y = 0
            elif self.snake_y < 0:#up
                self.snake_y = 0
                c.SPEED_X = 0
                c.SPEED_Y = 0
            
            """
            Display Updade <- fps in looping
            """
            pg.display.update()