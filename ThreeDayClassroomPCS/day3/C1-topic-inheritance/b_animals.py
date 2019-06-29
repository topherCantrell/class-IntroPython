# Baseclass of all animals. Contains common methods for all animals,
# but specific types of animals can override these.

class Animal:

    def __init__(self):
        print('Making an animal')

    def say_hi(self):
        # Isn't really a public method here. Other languages
        # allow us to make this virtual -- no implementation.
        # We would usually raise an exception here
        # raise Exception('You should override this')
        print('uhhhh?')

# Dog extends (adds to) Animal. Dog derives from Animal. Animal is the baseclass.
# Shown in a family tree with the base at the top, Animal is the "super" class.
# We also say Dog is the "subclass". We make this a verb -- we are subclassing
# Animal to make Dog. Dog inherits from Animal. Dog IS-A Animal (plus
# maybe more).

# Inheritance: you can't take things away. Only add things.


class Dog(Animal):

    def __init__(self):
        # First thing in your __init__ is to call your baseclass's __init__
        # This is the python3 syntax. It looks different in python2 and in
        # other languages
        super().__init__()
        print('Making a dog')

    def say_hi(self):
        # This overrides the default in Animal
        print('Bark Bark')

    def fetch(self):
        # This is new to Dog (not all animals)
        print('Here you go')


# Wolf extends Dog (which extends animal)
class Wolf(Dog):

    def __init__(self):
        super().__init__()
        print('Making a wolf')

    def say_hi(self):
        print('Arrroooooooo')

# Another kind of Animal


class Human(Animal):

    def __init__(self):
        super().__init__()
        print('Making a human')

    def say_hi(self):
        print('Hello')

# MULTIPLE-INHERITANCE (danger). This class picks up
# methods from Human and Wolf (you can call fetch on it).


class Werewolf(Human, Wolf):

    def __init__(self):
        # Which baseclass is called? You want both, right?
        super().__init__()


#a = Werewolf()

# Which 'say_hi' is called? Wolf? Human? Both? Neither? A
# new function that depends on the state of the object?
# a.say_hi()

# Animal should be an interface! No implementation -- no variables -- just a list of
# functions. An "informal" -- no need to have anything in code. We just "know" what
# it has.

# Formal:

# http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/
