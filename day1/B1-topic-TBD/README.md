# Variables and Functions

## Syllabus
  * Variables, Operations, Types, input()
  * Functions, Local Variables, Command-line Arguments
  * Refactoring
    - Chapter 1: 5
    - Chapter 2: 1, 2, 3, 5
    - Chapter 3: All Sections
    - Chapter 5: 11
    - Chapter 6: 1, 2, 3, 4, 5, 6,
    
## Teach Functions First

Lines of code are grouped together in a function. A function has a name.
A function has a list of parameters passed to it (might be none). A 
function may return a value.

You know about the `print` function. You pass a value into it and it prints
the value on the screen.

```python
# What comes out on the screen?
print(27)
print('Hello World')
```

### Defining Functions

You define your own functions with the "def" keyword

```python
def say_hi():
  print('Hello')
  print('There')
```

Rules:
  - Must start with def
  - Name must start with a letter, thn can use numbers
  - Open parenthesis, parameters (if any) close parenthesis:
  - Colon
  - Indented (other languages use {..})
  - Recommended: lowercase with "_" between words

Now you can use `say_hi` like you use print.

```python
# What comes out on the screen?
print('Here')
say_hi()
print('There')
say_hi()
```

### Functions calling functions

Work this example showing the refactoring.

Introduce the stack -- keeping track of where the program goes back to.

```python
# functions.py
def say_ha_why():
    print("HA!")
    print("Why,")
    
def say_hi():
    #print("HA!")
    #print("Why,")
    say_ha_why()
    print("Hello")
    print("There")

def say_bye():
    #print("HA!")
    #print("Why,")
    say_ha_why()
    print("Bye")
    print("Bye")
    
def come_and_go():
    say_ha_why()
    say_hi()
    say_bye()
    say_ha_why()
    
print('Start')
say_hi()
print('Done')

# Now show the refactor

print('Start')
say_ha_why()
come_and_go()
print('Done')
```

Must be defined before you call them. Not necessary in order in the file.

## Comments

The '#' ... follows bash shells in linux so the sh-bang line will work

No multi-line comment. You will see multi-line strings. Explain.

## Variables

Local variables are hidden in the function. Other functions can have the
same variable names. The variables go away when the function returns.

Variables are kept on the stack along with the return info. Work example:

```python
# variables.py
def say_hi():
    print('Hello')
    a = 5
    b = 6
    # Re-work example with "say_bye" here
    c = a + b
    print(c)
    
def say_bye():
    print('Bye')
    a = 2
    b = 6
    c = a + b
    print(c)
    
# Show stack

print('Start')
say_bye()
print('Done')
```

## Parameters Passed to Functions
```
# params.py
def add_two(a,b):
    # local variables a and b are created here
    # the incoming values are COPIED to the locals
    c = a + b
    print(c)
    a = 2 # Doesn't affect the caller
    b = 4
    
a = 7
b = 8
add_two(a,b)

add_two(10,20)
```

## Returns From Functions

```
# rets.py
def say_hi():
    print("Hello")
    # Return is automatically added
    return

def add_two(a,b):
    c = a + b
    # This is how you return a value
    return c

say_hi()

x = add_two(3,4) # Return value is copied into x
print(x)

y = add_two(x,x)
print(y)
```

Can return strings too.

Pick up `input` here.

## Expressions and Substitution
```
# exp.py
def add_two(a,b):
    print("Adding",a,b) # multiple things on a line
    c = a + b
    return c

x = add_two(1,2)
y = add_two(3,x)

# Could substitute in:

y = add_two(3, add_two(1,2))
print(y)

z = add_two(add_two(1,2),add_two(3,add_two(4,5)))
print(z)

# The computer calls the functions as needed to make the arguments to
# call the other functions. It starts left to right. Show the print.

# Do you like this compact expression? Or do you like to separate the
# steps out into local variables?
```

## Data Types (string, number, int, boolean)

```
# At the interactive prompt

# For demo ... notice the change of prompt
def do_stuff():
    aslkdfj
    asdf
    asdf
    asdf
    
do_stuff()

a = 5
type(a)

>>> a = 5
>>> type(a)
<class 'int'>
>>> type(5)
<class 'int'>
>>>
>>> a = 1.4
>>> type(a)
<class 'float'>
>>>
>>> a = True
>>> type(a)
<class 'bool'>
>>>
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>>
```

Math must be performed on numbers -- not strings.

```
>>> a = 'hello'
>>> b = 5 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
>>> a = '12'
>>> b = 5 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
>>> c = int(a)
>>> a
'12'
>>> c
12
>>> b = 5 + c
>>> b
17
>>>
```

Special string operation "+" for append (operator overloading). Both
terms must be strings.

And "*" ... string and int

```
>>> a = 'hello'
>>> b = 'world'
>>> c = a + b
>>> c
'helloworld'
>>>
>>> a * 5
'hellohellohellohellohello'
>>>

```