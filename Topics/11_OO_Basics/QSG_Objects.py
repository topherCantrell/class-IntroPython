# Objects

class Robot:
    
    # Constructor
    def __init__(self,x=0,y=0):
        self.x_pos = x
        self.y_pos = y
    
    # Methods take a pointer (usually named 'self')
    def say_hi(self):
        print('hi from',x,y)
    
    def move_to(self,x,y):
        self.x_pos = x
        self.y_pos = y
        # Methods calling other methods
        self.say_hi()
        
# Inheriting from Robot

class ImprovedRobot(Robot):
    
    # Adding functionality
    def fire_torpedos(self):
        pass
    
    # Overriding old things with new
    def say_hi(self):
        print('I AM MUCH IMPROVED')
        
r = Robot()
# or
r = ImprovedRobot()

# Polymorphism ... the object behaves differently depending on what
# it is. I just care that it can "say_hi". I don't care what it does.
r.say_hi()