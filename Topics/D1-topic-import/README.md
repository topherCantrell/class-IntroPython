# Import is a verb

## Syllabus

  * import is a Verb
  * Modules, __init__, __name__
  * Import Options

## Basics

Start with "importverb.py", "module_one.py", and "module_two.py".

Show pulling and using functions them in to importverb. This is the usual case. Creates a variable
with the module_name and adds all contents to that name. Access with the "." operator.

```python

#module_one.py
def say_hi():
  print('Hello from module one')

def add_two(a,b):
  return a+b
  
#module_two.py
def say_hi():
  print('Hello from module two')
  
#importverb.py

import module_one
import module_two

a = module_one.add_two(1,2)
print(a)
module_one.say_hi()
module_two.say_hi()

```

In other languages, "import" or "include" is used by the compiler. It has no meaning at runtime. But in python, it is a command. The module is not parsed until the import runs. Try moving the "module_two.say_hi()" above its import.

The import also runs all the code in the module.

```python

#module_one.py
def say_hi():
  print('Hello from module one')
  
def add_two(a,b):
  return a+b


# This is code out in the "global" space of the file
print("Module one is loading")


def add_two(a,b):
  return a+b
  
#module_two.py
def say_hi():
  print('Hello from module two')
  
# This is code out in the "global" space of the file
print("Module two is loading")
  
#importverb.py
import module_one
module_one.say_hi()

import module_two
module_two.say_hi()

# It is only loaded once. The system remembers.
import module_one
import module_one
import module_one

# Show running modules separately
```

## Packages

Add "pack_a" and "pack_a_sub". You have to import them separately -- not a recursive (there
is a way to specify this).

Add "__init__.py" to each. A way to have "package-level code" run when loaded.

## FROM, AS and wildcard

Show collisions.

## RANDOM

Look at the "random" module. Python has a rich library for you to use -- you just have to know what's there.