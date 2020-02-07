__author__ = "jacksonsr45@gmail.com"
from game import constants as c

class Draw_Snake(object):
    def draw_snake(self, pg, root, __snake_, width, height):
        """
        Drawing snake in screen
        receive values the __init__
        :root: screen or root for snake
        :__snake_: x and y to snake in screen
        :width: pixels in width
        :heigth: pixels in heigth
        """
        for row in __snake_:
            pg.draw.rect(root, c.BLACK, [ row[0], 
                            row[1], c.PX, c.PX])        