class Point:
    
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def print_info(self):
        #print('(',self._x,',',self._y,')')
        print('(',self.get_x(),',',self.get_y(),')')
        

from points import Point

import random

class RNDPoint(Point):
    
    def __init__(self):
        super().__init__(0,0)
        
    def get_x(self):
        return random.randint(0,9)
    
    def get_y(self):
        return random.randint(0,9)
    
    