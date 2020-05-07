# Lists and Tuples

## Syllabus

  * Lists and Tuples, len(), slicing
  * for-each
  * Algorithms
    - Chapter 10: All Sections
    - Chapter 12: All sections
    
## Lists

Lists are objects. We create an empty list object like this:

```python
p = list() # other languages would be p = new list()

my_stuff = ... # better naming

```

Then we call functions ON the object. Not just a function like print, but a function
that is tied to the object. We call these methods, but they work the same as functions.

```python
# Appending things to the list

p.append(1)
p.append('hello')
p.append(True)

# Accessing parts of the list

p.__len__() # 3

p.__getitem__(0) # 1
p.__getitem__(1) # 'hello'
p.__getitem__(-1) # True
p.__getitem__(-3) # 1
p.__getitem__(4) # ERROR list index out of range
p.__getitem__(-4) # ERROR

p.__repr__() # Method to make a nice string representation
"[1, 'hello', True]"

p.__setitem__(1,'world')
p.__delitem__(2) # index
p.__repr__()
"[1, 'world', True]"
```

In all of these operations, we are asking the object to do things. We are calling methods on the object. The python compiler
gives us some help.

  - p[i] uses `__getitem__` or `__setitem__` depending the direction
  - len(p) calls `__len__` for us
  - repr(p) calls `__repr__` for us (this is what the repl uses)
  - in calls `__contains__` for us
  - del calls `__delitem__` for us

So the usual syntax:
  
```python
p = list()
p.append('hello')
p.append('world')
print(len(p))
a = p[0]
p[1]='False'
p.append(25)
print(p)
p.insert(1,400)
del p[2]
p.__contains__(4)
4 in p
p.index(2)
```

And python has a "literal" definition for lists. Instead of using 'list()' you will almost always do this:

```python
p = ['hello', 'world']
p.append('wow') # Does this modify p? NO ... it modifies the object pointed to by p
print(p)
q = p + [1,2] # The "__add__" method creates a new list with the items of both
print(p) 
print(q)
a = [] # make an empty list
```

## Algorithms

Now we can write code to loop over a list.

```python

m = [5,3,6,1,1,2]

i = 0
while i<len(m):
  print('>',m[i])
  i = i + 1 # What if you forget this?
  
for i in range(len(m)):
  print('>',m[i])
  
for a in m:
  print('>',a)

```

How about a function to find the largest value?

```python
def find_largest(m):
  ret = 0 # m[0] ... what happens if empty list is passed in?
  i = 0
  while i<len(m):
    if m[i]>ret:
      ret = m[i]
    i += 1
  return ret
  # Show better syntax
  
nums = [0,2,5,1,5,100]
a = find_largest(nums)
print(a)

a = find_largest([-1,-2,-3])
print(a)
```

Other fun: sorting algorithms like the bubble sort

## Tuples

Tuples are like lists but you can't change/append them. They use "()" instead of "[]".

```python
p = (1,2,3)
p[1] = 4 # ERROR

# Has __add__ method:
q = p + (4,5,6)
```

## Packing and unpacking

```python
def get_numbers():
  a = [1,2,3,4]
  return a
  
i = get_numbers() # What is i? A list of 4 things
i[2] = ? # 3

a,b,c,d = get_numbers()

a,b = get_numbers()

def get_nums_two():
  return 5,6,7,8
  
p = get_nums_two() # tuple
p[2] = ? # 7
a,b,c,d = get_nums_two()
```

## Remember these are pointers

First, work through this in code. Then show the pointers.

SEE snippets.pptx

```python
p = [1,2,3,4]
h = [25,35]

p[2] = h

print(p)

x = p[2]
x[1] = 50

print(p)

p[2][1] = 60

print(p)
```

Do you need to think about this when you write simple programs? Definitely not.
But if you find yourself in complex situation where you are getting 
unexpected results, this might be why.