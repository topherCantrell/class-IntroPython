# Dictionaries

Dictionaries are key/value maps. You show the dictionary a key and a value and say "this key maps to this value".
Then later you ask the dictionary "now what value went with this key?" and it tells you.

Keys must be unique. Values can map to multiple keys. Keys can be most anything -- strings are common key types.

The API is very much like a list except with keys instead of indices. There is no "order" to a dictionary. It stores
in whatever order it wants.

Creating a dictionary object:

```
>>> d = dict()
```

Associating keys and values:

```
>>> d.__setitem__('name','Chris')
>>> d['age'] = 25
>>> d['cool'] = True
>>> d['age'] = 45
```

Literal definition:

```
>>> d = {'name' : 'chris', 'age' : 45, 'cool' : True}
>>> d = {
...     'name' : 'chris',
...     'age'  : 45,
...     'cool' : True
...     }
```

"Looking up" values:

```
>>> d.__getitem__('age')
45
>>> d['name']
'Chris'
```

String representation:

```
>>> d.__repr__()
"{'name': 'Chris', 'age': 45, 'cool': True}"
>>> print(d)
{'name': 'Chris', 'age': 45, 'cool': True}
```

Removing items:

```
>>> d.__delitem__('cool')
>>> d
>>> "{'name': 'Chris', 'age': 45}"
>>> del d['age']
>>> "{'name': 'Chris'}"
```

Does the collection contain:

```
>>> d.__contains__('cool')
False
>>> 'cool' in d
False
>>> if 'cool' in d:
>>>     print('You are cool')
```

No such item:

```
>>> d['phone']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'phone'
```

Iteration:

```
>>> for k in d:
...     print(k)
...
name
age
cool

>>> for k in d:
...     print(k,d[k])
...
name chris
age 45
cool True

>>> d.keys() # Returns list of keys
dict_keys(['name', 'age', 'cool'])
>>> d.values() # Returns list of values
dict_values(['chris', 45, True])
>>> d.items() # Returns list of key/value mappings
dict_items([('name', 'chris'), ('age', 45), ('cool', True)])

>>> for item in d.items():
...   print(item)
...
('name', 'chris')
('age', 45)
('cool', True)

>>> for k,v in d.items():
...   print(k,v)
...
name chris
age 45
cool True
```

## An example -- counting duplicates in a list

```python
data = 'asdfasdfjlkjalsdfjwerltkjscflkjasdflkjweqrtlkasdfjlkasjdf'

def count_items(d):
    ret = {}
    for i in d:
        ret[i] = 0
    for i in d:
        ret[i] = ret[i] + 1
        
    ret = {}
    for i in d:
        if i in ret:
            ret[i] += 1
        else:
            ret[i] = 1
        
    return ret
        
r = count_items(data)
print(r)

r = count_items(['hello','there','world','hello','hello'])
print(r)

r = count_items([1,2,2,1,6,5,8,6,1])
print(r)

r = count_items([True,'hello',1,1,'hello',True])
print(r)
```

## Nested containers

```
>>> a = [1,2,3]
>>> a[1] = ['hello','world']
>>> a
[1, ['hello', 'world'], 3]
>>> a[0]
1
>>> a[1]
['hello', 'world']
>>> a[1][0]
'hello'
>>>
```

Looks like a multidimensional array, but ...

```python
'''
  0  1
  2  3
  4  5
'''

a = [
    [0,1],
    [2,3],
    [4,5]
    ]

print(a)

print(a[1][1]) # Row 1 column 1

a[1].append(100) # Now ragged

print(a)
```

Mixture of things (keep in mind ... just pointers)

```python
b = {
    'name' : 'chris',
    'numbers' : [1,2,3,4]
}

print(b['numbers'][2])

c = {
    'name' : 'chris',
    'phones' : {
        'work' : 1234,
        'home' : 5678
    }
}

print(c['phones']['work'])
```

