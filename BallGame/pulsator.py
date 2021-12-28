# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole): 
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.check_time = 0
    def update(self):
        if self.radius == 0:
            model.remove(self)
        self.get_remove = Black_Hole.update(self)
        if len(self.get_remove) > 0:
            times = len(self.get_remove)
            self.radius += times * 0.5
            self.change_dimension(times, times)
            self.check_time = 0
        else:
            self.check_time += 1
            if self.check_time == 30:
                self.radius -= 0.5
                self.change_dimension(-1, -1)
                self.check_time = 0
        return self.get_remove