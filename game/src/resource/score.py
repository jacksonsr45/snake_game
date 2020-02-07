__author__ = "jacksonsr45@gmail.com"
from .import*
from game import constants as c

class Score(object):
    def __score__(self, pg, bg, score):
        """
        Booting Score with font and color: 
        """
        score_font = pg.font.SysFont("comicsansms", 35)
        value = score_font.render("Score: " + str(score), True, c.VERDE)
        bg.blit(value, [0, 0])