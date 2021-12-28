# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

import math
from prey import Prey
import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, width = 10 ,height = 10,angle = 0, speed = 5)
        self.randomize_angle()
        self._color = 'red'

    def update(self):
        get_check = random.random()
        if get_check <= 0.3:
            self._angle += random.uniform(-0.5,0.5)
            self._speed += random.uniform(-0.5,0.5)
        self.move()
    

    def display(self,canvas):

        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
