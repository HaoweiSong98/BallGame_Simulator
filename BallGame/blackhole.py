# Black_Hole inherits from only Simulton, updating by finding/removing
#   any Prey-derived class whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, width = 20, height = 20)
        self._color = 'black'
        
    def update(self):
        get_prey_set = model.find(Prey)
        self.get_remove = set()
        for b in get_prey_set:
            if self.constains(b.get_location()):
                self.get_remove.add(b)
        for b in self.get_remove:
            model.remove(b)
        return self.get_remove

    def display(self, canvas):
        get_xy= self.get_dimension()
        canvas.create_oval(self._x- get_xy[0]/2      , self._y-get_xy[1]/2,
                                self._x+get_xy[0]/2, self._y+get_xy[1]/2,
                                fill=self._color)

    def constains(self, xy):
        return self.distance(xy) < self.radius

