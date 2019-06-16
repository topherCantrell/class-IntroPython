# Control Flow

## Syllabus

  * Boolean, Logical Operators
  * if/elif/else
  * while/break/continue
    - Chapter 5: 2,3,4,5,6,7,8,9,10
    - Chapter 7: 1,2,3,4,6
    
## Booleans

  * True
  * False

## IF/ELIF/ELSE

Introduce `pass` here.

```
# ifelse.py
# Two kinds of jumps ... forwards (skip over code) and backwards (repeat code)

# ## THINK PYTHON: CH5 Conditionals and Recursion

# Forward skips are IF/ELIF/ELSE
# Backward skips are loops WHILE/FOR

print('start')
a = 7
if a==7:
  print('It is seven')
print('done')

# Add the else

a = 7

print('start')

if a==5:
    print('FIVE')
else:
    if a==6:
      print('SIX')
    else:
      if a==7:
         print('SEVE')
      else:
         print('OTHER')

# Better using elif

if a==5:
    print('FIVE')
elif a==6:
    print('SIX')
elif a==7:
    print('SEVE')
else:
    print('OTHER')
    
print('done')
        
# if a>=1 and a<=10:

if a>5 and a<4:
    print('wow')
    
if not a>5:
    print('pass')
    
# These expressions are booleans

# Logical operators
# ==, !=, <, <=, >, >=

x = a>5 # True or False

if x:
    print('Pass')

def is_it_five_forty():
    return True    
if is_it_five_forty():
    print('DING DING DING')
    
# Python will asses the "true-ness" of a value
if 1:
    print('1 is True')

if not 0:
    print('0 is False')
  
s = 'j'  
if s:
    print('non-empty string is True')
    
s = ''
if not s:
    print('empty string is False')
```

## WHILE/BREAK/CONTINUE

Backwards to repeat code (loops).

```
# loops.py

# ## THINK PYTHON: CH7 Iteration

# The WHILE loop is the most primitive. You must initialize the loop variable
# and you must change the loop variable as needed.

# BREAK looks back up to the first loop it finds and breaks out
# CONTINUE looks back up to the first loop it finds and continues

"""
x = 0
while x<5:
    print(x)
    x += 1
"""

"""
x = 0
while x<5:
    print('Top')
    x += 1
    if x==3:
        continue
    print(x)
"""

"""
x = 0
while x<5:
    print('Top')
    x += 1
    if x==3:
        break
    print(x)
"""
```
