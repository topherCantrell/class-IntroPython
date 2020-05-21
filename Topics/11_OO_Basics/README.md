# Object Oriented Programming

Python is extremely OO ... everything we do is with objects. The "dot" operator means you
are working with an object on the left and its data or functions on the right.

Objects are little islands of data. They each have their own personal memory storage.

Objects live on the heap. We use pointers to them.

CLASS is the cookie-cutter for memory. We use CLASSes to stamp out INSTANCES of the class -- to
stamp out OBJECTS.

## Making and using a class

```python
class Robot:
    
    def say_hi(p):
        print('Beep boob beep')
        print(id(p))
        

rob = Robot()
print(id(rob))
bob = Robot()
print(id(bob))

rob.say_hi()

bob.say_hi()
```

You define functions within the scope of the class.

All of these functions have the first argument as the pointer to the object. This
is what is on the left of the dot. The pointer on the left is passed to the function
as the first argument.

I called it "p" here. Other languages name the argument "this". Python prefers you
to use the name "self". It's just a pointer. Nothing special about the name "self". It
isn't a keyword.

These are just plain old functions here. They always take a pointer to the target object.
We call these "methods". You'll hear me say "functions" occasionally.

Naming conventions:
  - Camel case (no '_')
  - Begin with upper case letter
  - Nouns
  - Methods are just functions ... named the same way (lower case letter verbs)

## OO programming is about the API -- what objects can do

```python
class Robot:
    
    def say_hi(self):
        print('Beep boob beep')  
        
    def move_to(self,x,y):
        pass
    
    def fire_laser(self,power):
        pass      
        

rob = Robot()
rob.say_hi()
rob.move_to(10,20)
rob.fire_laser(0.1)

# These really are just functions
Robot.fire_laser(rob,0.5)
```

We use these objects like they have functions inside them ... like each object has 
its own code, but really they all share the same code. That's why we pass "self" in
so the code can identify the target memory (shortly).

## Methods calling methods

```python
class Robot:
    
    def _move_left_leg(self):
        pass
    
    def _move_right_leg(self):
        pass
    
    def say_hi(self):
        print('Beep boob beep')  
        
    def move_to(self,x,y):
        self._move_left_leg()
        self._move_right_leg()
    
    def fire_laser(self,power):
        pass      
```

The "_" is a hint to the developer that they might not should use these. Private API vs public API.

Your methods have that first parameter pointer, so you have to pass the parameter you
were given to others. Remember, "self" is just a variable name ... not a keyword. This
is just calling a method on an object ... it just happens to be yourself.

## Data with the objects

Objects have different state. Like our robot. When we tell it to move, it keeps up
with that. That's what "self" really is -- a pointer to the memory for the object.

```python
class Robot:
    
    def _move_left_leg(self):
        pass
    
    def _move_right_leg(self):
        pass
    
    def say_hi(self):
        print('Beep boob beep from',self.x_pos,self.y_pos)  
        
    def move_to(self,x,y):
        self._move_left_leg()
        self._move_right_leg()
        self.x_pos = x
        self.y_pos = y
    
    def fire_laser(self,power):
        pass      
        

rob = Robot()
rob.move_to(10,20)
rob.say_hi()

jan = Robot()
jan.move_to(40,35)
jan.say_hi()

pat = Robot()
pat.say_hi() # Oops
```

How can we ensure that all objects have initial state?

## Constructors

```python
class Robot:
    
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
```

Require initial value

```python
class Robot:
    
    def __init__(self,x,y):
        self.x_pos = x
        self.y_pos = y
```

Default values. This is NOT special for classes. This works for all functions.

```python
class Robot:
    
    def __init__(self,x=0,y=0):
        self.x_pos = x
        self.y_pos = y
```

## It's about telling objects to do things

```python
    def fire_laser(self,power):
        print('Sterilize')      

def cleanse_covid(r,x,y):
    r.say_hi()
    r.move_to(x,y)
    r.say_hi()
    r.fire_laser(1)
    r.move_to(0,0)        

rob = Robot(0,0)

cleanse_covid(rob,x,y)
```

## Inheritance and polymorphism

The new and improved robot has photon torpedos.

```python
class ImprovedRobot(Robot):
    
    def fire_torpedos(self):
        print('Torpedos away')

hank = ImprovedRobot(1,1)
hank.say_hi() # Can I do this?
hank.fire_laser(.5)
hank.fire_torpedos()
```

Inheritance adds. But you can't take anything away.

Can I call `cleanse_covid` with this?

The new and improved robot has a new way of moving:

```python
class ImprovedRobot(Robot):
    
    def fire_torpedos(self):
        print('Torpedos away')
        
    def move_to(self,x,y):
        print("I'd rather fly!")
        # activate thrusters
        self.x_pos = x
        self.y_pos = y
```

The `cleanse` method doesn't care WHAT the move_to function does ... just that
the object has one.

Objects with the same interface but different behaviors. Fancy name "polymorphism".

# OO topics in advanced
  - Encapsulation (hide the data behind methods)
  - Multiple inheritance
  - Composition vs inheritance
  - Using `super()` to access your baseclass
  - Design Patterns (Gang-of-Four book)
  