

class Point:

    # def __init__(self, x, y):
    #    self._x = _x
    #    self._y = _y

    def init(self):
        self.x = 0
        self.y = 0

    def change(self, x, y):
        self.x = x
        self.y = y

    def print_me(self):
        print('(', self.x, ',', self.y, ')')

    # Getters and setters

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x


point_a = Point()

# Note that the thing on the left is passed in as "self" automatically. Passed as an argument, but
# you don't do that explicitly in the argument list.

point_a.init()
point_a.change(10, 20)

# These functions-in-a-class that take "self" are called "methods"

point_a.print_me()

#point_b = Point(5, 6)
# point_b.print_me()

# We don't think about how the data is stored. We think only about what we can tell
# these objects to do ... change yourself, print yourself, convert yourself to upper
# case, find a substring within you, write data to the file you have open, etc