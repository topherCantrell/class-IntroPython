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
    
## We Should Teach Functions First!

We used to teach variables and types first.

### Using Functions

Lines of code are grouped together in a function. A function has a name.
A function has a list of parameters passed to it (might be none). A 
function always returns a value (None by default).

You know about the `print` function. You pass a value into it and it prints
the value on the screen.

```python
# What comes out on the screen?
# Comments ... single line
print(27)
print('Hello World')
print('Hello','There','World')

# keyword arguments

print('Hello','There','World',sep='###')

x = print(27)
# What's in X?
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
  - Name must start with a letter, then can use numbers
  - Open parenthesis, parameters (if any) close parenthesis:
  - Colon
  - Indented (other languages use {..})
  - Recommended snake-case: lowercase with "_" between words

Now you can use `say_hi` like you use print.

```python
# What comes out on the screen?
print('Here')
say_hi()
print('There')
say_hi()
```

### Functions calling functions

```python
def say_hi():
    print("HA!")
    print("Why,")
    print("Hello")
    print("There")
    
def say_bye():
    print("HA!")
    print("Why,")
    print("Bye")
    print("Bye")
    
def come_and_go():
    say_hi()
    say_bye()
    
print('Start')
say_hi()
print('Done')    
```

And the refactor:

```python
def say_ha_why():
    print("HA!")
    print("Why,")
    
def say_hi():    
    say_ha_why()
    print("Hello")
    print("There")

def say_bye():    
    say_ha_why()
    print("Bye")
    print("Bye")
```

Introduce the stack -- keeping track of where the program goes back to.

SEE snippets1.pptx

Show this in the debugger. Show the jumping around.

Must be defined BEFORE YOU USE THEM. Not necessary in order in the file.

```python

# This is just a definition. The compiler processes it.
def funA():
    funB()
    print("A")
    
This code runs as parsed, and funB is not defined yet.
# funB()
    
def funB():
    print("B")
    
# Everything is defined before funA calls funB
funA()
```

## Comments

The '#' ... follows bash shells in linux so the sh-bang line will work

No multi-line comment. You will see multi-line strings.

```python

a = 'hello there world'
print(a)

a = 'hello\nthere\nworld'
print(a)

a = '''hello
there
world'''
print(a)

def my_function():
    print('hello')
    
    # What are these? Just wasted computations. But legal
    5    
    8+10    
    'wow'
    
    '''and
    this
    now'''
    
    # can wrap code in multi-line comments to remove it
    # IDEs can do "blocks of #"
```

## Variables

SEE snippets2.pptx

Local variables are kept on the stack along with the return information.
When a function returns, all of its local variables go too.

When you call a function, it does not have access to your local variables.
The only local variables the CPU can see are the ones in the function it
is currently running. Period. 


```python
def oh_man():
    a = 20
    b = 30
    c = 40
    
def say_hi():
    print('Hello')
    a = 5
    b = 6
    oh_man()
    c = a + b
    print(c)

say_hi()
print('Done')
```

Variables are automatically created when you assign to them. They must
be created before you can read from them.

## Parameters Passed to Functions

SEE snippets2.pptx

Arguments become local variables. The VALUE of the passed argument is
copied in. Now, before you get excited about pass-by-value, all values
are pointers. So really we are passing by reference!

We'll look more at the stack/heap next time.

`global` variables later.

```python
def add_two(a,b):    
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

```python
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
```python
def add_two(a,b):
    print("Adding",a,b)
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

## More

If there is time, we can do id(x) and dir(x) here.
