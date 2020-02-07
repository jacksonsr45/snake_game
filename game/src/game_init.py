__author__ = "jacksonsr45@gmail.com"

from game import constants as c



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
        Init Values default for Snake
        :p_snake: This is value in pixels for snake
        :pos_x: This is pos in X in screen  
        :pos_y: This is pos in Y in screen
        """
        self.p_snake = 10
        self.pos_x = c.WIDTH/2
        self.pos_y = c.HEIGHT/2

        """
        Init self.in_game with True 
        While is true in game else out game
        """
        self.in_game = True
        
        self.loop_game()

    def loop_game( self):
        """
        This loop for game 
        While in_game True
        :requere: self.in_game
        :return: self.in_game  
        """
        while self.in_game:
            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    self.in_game = False
                self.pg.display.update()

            self.back_ground.fill(c.WHITE)
            self.draw_snake(self.back_ground, self.pos_x, 
                            self.pos_y, self.p_snake, self.p_snake)
            

    def draw_snake(self, root, pos_x, pos_y, width, height):
        """
        Drawing snake in screen
        receive values the __init__
        :root: screen or root for snake
        :pos_x: pos_x in root
        :pos_y: pos_y in root
        :width: pixels in width
        :heigth: pixels in heigth
        """
        self.pg.draw.rect(root, c.BLACK, [ pos_x, 
                            pos_y, width, height])