# Hunter inherits from the Pulsator (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator, Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        width = self._width
        height = self._height
        Mobile_Simulton.__init__(self, x, y, width, height, angle = 0, speed = 5)
        self.randomize_angle()
    
    def update(self):
        get_all_prey = model.find(Prey)
        get_list = list(get_all_prey)
        if len(get_list) != 0:
            lowest = get_list[0]
            for b in range(len(get_list)):
                if self.distance((get_list[b]._x,get_list[b]._y)) < 200:
                    if self.distance((get_list[b]._x,get_list[b]._y)) < self.distance((lowest._x,lowest._y)):
                        lowest = get_list[b]
                        
            self.set_angle(atan2(lowest._y - self._y, lowest._x - self._x))
        Pulsator.update(self)
        self.move()
        
