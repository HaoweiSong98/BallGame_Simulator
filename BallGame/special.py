# If the Prey simulton touch Special simulton they will be change color to yellow 
from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
import model


class Special(Pulsator, Mobile_Simulton):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, angle = 0, speed = 5)
        self.randomize_angle()
        self._color = 'yellow'
    def update(self):
        self.move()
        get_prey_set = model.find(Prey)
        self.get_color = set()
        for b in get_prey_set:
            if self.constains(b.get_location()):
                self.get_color.add(b)
        for b in self.get_color:
            b._color = self._color