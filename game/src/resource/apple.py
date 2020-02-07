__author__ = "jacksonsr45@gmail.com"

from game import constants as c
from .import*

class Draw_Apple(object):
    def __apple__(self, pg, root, apple_x, apple_y,
                    width, height):

        """
        Drawing apple in screen
        receive values the __init__
        :root: screen or root for apple
        :pos_x: pos_x in root
        :pos_y: pos_y in root
        :width: pixels in width
        :heigth: pixels in heigth
        """
        apple = pg.draw.rect(root, c.RED, [ apple_x, 
                            apple_y, width, height])
        return apple
