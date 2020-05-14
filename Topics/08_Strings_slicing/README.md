# Strings

There is no 'character' type. There are only strings!

What we think of a "strings" is just a collection of single-character strings!

A character is a string of length one.

It is a bit mysterious ... a string is a sequence of strings. Seems like a chicken and egg problem.

## Creating strings

```
>>> a = str()
>>> a
''
>>>

>>> a = 'hello world'
a
'hello world'
```

## Multiline strings

```
>>> a = '''This
... is
... a
... test'''
>>> a
'This\nis\na\ntest'  # This is the "repr" of the string
>>> print(a)         # This is the "str" of the string
This
is
a
test
>>>

>>> >>> a = 'Hello\nthe\tre\nworld'
>>> print(a)
Hello
the     re
world
```

## Any value

Under the covers, letters are mapped to numbers. So a character is really just a number.

```
>>> a = 'A'
>>>
>>> ord(a) # ordinal (history way back to pascal)
65
>>> chr(65)
'A'
>>> ord('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 5 found
>>>

>>> str(65) # Make a string ... not a character
'65'
```

## Accessing the values

EXACTLY as you would a list:

```
>>> a = 'hello world'
>>>
>>> a[0]
'h'
>>> a[6]
'w'
>>> a[-1]
'd'
```

## Strings are immutable

There is no `a[6] = 'T'`

There is NOTHING you can do to change the value of a string. NOTHING.

## Methods

```
len(a)

dir(a)
```

Look at all that stuff. Experiment with:
  - upper
  - lower
  - strip
  - is...
  - rjust/ljust
  - replace
  - title
  - center
  
## Find vs index

```
>>> a = 'hello'
>>> a.find('X') # Just for strings ... no lists
-1
>>> a.index('X')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

```
  
## Slicing

```
>>> a = [1,2,3,4,5]
>>> b = a[2:4]
>>> b
[3, 4]
```

Start defaults to '0'. End defaults to end of string.
  
You can add lists (and strings):

```
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = a
>>> a = a + b
>>> # What's in c? What's in a?
```

```
>>> a = [1,2,3,4,5]
>>> a[0:2] + a[-2:]
[1, 2, 4, 5]
>>> b = a[2]
>>> b
3
```

This all works with strings the same way.

## Common use -- replacing things in a string:

```python
a = 'Hello <<NAME>>. How are you <<NAME>>?'

a.replace('<<NAME>>','Chris')

print(a)

# WHAT THE HECK? Ahhhhh!

b = a.replace('<<NAME>>','Chris')

print(b)
```

I just chose '<<' and '>>'. Could be anything. Even '|NAME|'.

How about a general purpose replacer.

```python
a = 'Hello <<NAME>>. I hear you like <<FOOD>> and have a pet <<ANIMAL>>'

def substitute_one_key(s,key,value):
  return s.replace('<<'+key+'>>',value)

# Call this for NAME, FOOD, ANIMAL
```

How about a dictionary ... replace all key/values in the string!

```python
a = 'Hello <<NAME>>. I hear you like <<FOOD>> and have a pet <<ANIMAL>>'

def substitute(s,items):
    for key in items:
      s = s.replace('<<'+key+'>>',items[s])
    return s
```

Can you make a list of all replacements from the string?

```python

def get_subs(s):
  pos = 0
  ret = []
  while True:
    i = s.find('<<',pos)
    if i<0: # not found
      return ret
    j = s.find('>>',pos)
    key = s[i+2,j]
    ret.add(key)
    pos = j+2
  
