# Exceptions

Common to most every language. Exceptions are a way of dealing with truly exceptional things (like disk problems).

In a nut shell, instead of checking return codes after every step of a process, you define a handler to jump to
if an exception occurs. Then your code proceeds normally without the wasted time/confusion checking every step.

Exceptions work with the call stack. If your function doesn't handle an exception, then it automatically 
"bubbles" back up to the caller ... and then its caller ... until it is either handled by your code or the VM,
which kills the program. We'll see what this means shortly.

You've seen exceptions:

```
>>> a = [1,2,3]
>>> a[50]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> 10/0

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

They say "Error", but those are what we call exceptions.

The `raise` keyword is how you cause one in your code. We say "raise an exception" or "throw an exception".

```
>>> raise IndexError('Neat, huh?')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Neat, huh?
>>> raise ZeroDivisionError('Impossible to do')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: Impossible to do
>>> raise ZeroDivisionError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError
```

You can define your own exception classes. We'll look at that after Object Oriented Programming.

# Basic try/catch syntax

```python
print('starting')

try:
    print('I am here')
    #a = 1 / 0
    print('And here')
except:
    print('Something bad happened')
    
print('finishing up')
```

If something goes wrong in the TRY block, then the code is aborted and the EXCEPT block runs.

```
print('starting')

try:
    print('I am here')
    b = [1,2,3]
    #a = 10/0 # ZeroDivisionError
    #a = crazy # NameError    
    #a = b[100] # IndexError
    #a = b.alkdsfjlaskdfj() # AttributeError
    print('And here')
#except:
#    print('First')
except NameError:
    print('Got a name error')
except IndexError:
    print('Got an index error')
except:
    print('Something bad happened')
    
print('finishing up')
```

Order matters. The first matching wins. Empty matches everything -- frowned upon. Usually:

```
except Exception
```

`Exception` is the base of all our common Errors.

# Exceptions and the Callstack

```python
def read_byte():
    print('Reading a byte')
    a = 0
    # If you wanted to return a code, what would it be?
    # How about in other functions? Show how that might
    # look.
    # raise Exception('disk error')
    print('Got the byte')
    return a

def read_word():
    print('Reading a word')
    a = read_byte()
    b = read_byte()
    print('Got the word')
    return a*256 + b

def read_long():
    print('Reading a long')
    a = read_word()
    b = read_word()
    print('Got the long')
    return a*65536+b

a = read_long()
print(a)
```

The read_byte() aborts everything. Look at the traceback:

```
Reading a byte
Traceback (most recent call last):
  File "D:\git\class-IntroPython\Topics\09_Exceptions\simdisk.py", line 23, in <module>
    a = read_long()
  File "D:\git\class-IntroPython\Topics\09_Exceptions\simdisk.py", line 18, in read_long
    a = read_word()
  File "D:\git\class-IntroPython\Topics\09_Exceptions\simdisk.py", line 11, in read_word
    a = read_byte()
  File "D:\git\class-IntroPython\Topics\09_Exceptions\simdisk.py", line 5, in read_byte
    raise Exception('disk error')
Exception: disk error
```

We can catch the exception in `read_byte`. But nothing we can do to recover.
Better to let the exception bubble up the stack.

Show catching it at various spots.

Best to let the caller to "read_long" figure out what to do with it.

# Finally

The `finally` section is always executed on the way out of the block. This is a good place to clean up resources
like a database connection or an open file.

# Try/Else

The `else` block happens if an exception doesn't. This isn't technically needed. You could move the code to the
end of the normal block. Other languages (C++, Java, Javascript) don't have else.

```
print('Start')
try:
    print('I am here')    
    #a = 10/0 # ZeroDivisionError    
    print('And here')
except Exception:
    print('Something bad happened')
else:
    print('Nothing bad happened')
finally:
    print('And always here')
print('Done') # How could this ever be skipped?
```

# Raise (re-raise)

The `raise` command by itself reraises the caught exception.

```python
try:    
    a = 10/0 # ZeroDivisionError
except:
    print('Something bad happened')
    raise
print('Never got here')
```

# Cost

The "normal" case of an exception is fast. But if an exception happens, the handling is generally very slow.

This is the case in Java and C++.

Don't use exceptions for things that you expect to happen. The python community seems to disagree with me. They
say to "get forgiveness instead of ask for permission". So they like this:

```python
b = [1,2,3,4]

try:
  x = b.index(20)
  print('Found it at',x)
except Exception:
  print('Did not find it')
```

Instead of this:

```
b = [1,2,3,4]

if 20 in b:
    x = b.index(20)
    print('Found it at',x)
else:
    print('Did not find it')
```

Under the covers, python uses exceptions to handle the end of a `for each` loop. I need to do some timing studies
and refine my view of exceptions in python.