# Tinkering with random

```
>>> import random
>>> dir(random)
['betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>>

>>> help(random.randrange)
Help on method randrange in module random:

randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
    Choose a random item from range(start, stop[, step]).

    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.

>>> random.randrange(0,10,2)
6
```

# What's the problem with randint?

```
>>> random.randint(1,100)
98
>>> random.randint(1,100)
9
>>> random.randint(1,100)
33
```

How can we tell what randint returns?

```
>>> random.randint(2,5)
# Over and over ... produces 2 and 5 ... both endpoints (inclusive)

```

# Choice and Shuffle

```
>>> a = ['one','two','three','four']
>>> a
['one', 'two', 'three', 'four']
>>> random.shuffle(a)
>>> a
['three', 'one', 'four', 'two']
>>> random.shuffle(a)
>>> a
['three', 'four', 'two', 'one']

>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.
    
>>> random.choice(a)
'four'
>>> random.choice(a)
'two'
>>> random.choice(a)
'four'
>>> random.choice(a)
'four'

# Strings are sequences
>>> a = 'hello world'
>>> random.choice(a)
'o'
>>> random.choice(a)
'h'
>>> random.choice(a)
'w'

>>> random.shuffle(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\tophe\AppData\Local\Programs\Python\Python38-32\lib\random.py", line 307, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment
```

What this means is that string has a `__getitem__` method to do `i=a[x]` but no `__setitem__` method to do `a[x]=i`.

Strings are readonly. They are immutable.
