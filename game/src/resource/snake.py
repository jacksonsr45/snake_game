__author__ = "jacksonsr45@gmail.com"
from game import constants as c

class Draw_Snake(object):
    def draw_snake(self, pg, root, pos_x, pos_y, width, height):
        """
        Drawing snake in screen
        receive values the __init__
        :root: screen or root for snake
        :pos_x: pos_x in root
        :pos_y: pos_y in root
        :width: pixels in width
        :heigth: pixels in heigth
        """
        snake = pg.draw.rect(root, c.BLACK, [ pos_x, 
                            pos_y, width, height])
        return snake