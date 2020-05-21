

class Robot:
    
    def __init__(self,x,y):
        self.x_pos = x
        self.y_pos = y
    
    def _move_left_leg(self):
        pass
    
    def _move_right_leg(self):
        pass
    
    def say_hi(self):
        print('Beep boob beep from',self.x_pos,self.y_pos)  
        
    def walk_to(self,x,y):
        self._move_left_leg()
        self._move_right_leg()
        self.x_pos = x
        self.y_pos = y
    
    def fire_laser(self,power):
        print('Sterilize')      
        
class ImprovedRobot(Robot):
    
    def fire_torpedos(self):
        print('Torpedos away')
        
    def walk_to(self,x,y):
        print("I'd rather fly!")
        # activate thrusters
        self.x_pos = x
        self.y_pos = y

def cleanse_covid(r,x,y):
    r.say_hi()
    r.walk_to(x,y)
    r.say_hi()
    r.fire_laser(1)
    r.walk_to(0,0)        


hank = ImprovedRobot(1,1)
hank.say_hi() # Can I do this?
hank.fire_laser(.5)
hank.fire_torpedos()

rob = Robot(0,0)

cleanse_covid(rob,100,200)
