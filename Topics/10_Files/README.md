# Files

```
This is a
testing file of
plain text.
```

# Reading a text file

```
>>>f = open('test.txt')
>>>dir(f)
[...,
'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 
'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 
'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 
'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 
'write_through', 'writelines']
```

Read the entire file into a string:

```
>>>f = open('test.txt')
>>>g = f.read()
>>> g = f.read()
>>> g
'This is a\ntesting file of\nplain text.'
>>> print(g)
This is a
testing file of
plain text.
>>> g = f.read()
>>> g
''

>>> f = open('test.txt')
>>> f.fileno()
4

# Notice the filenumber. Was 3. We didn't CLOSE the first file.

>>> g = f.read()
>>> f.close()

# Remember to close.

>>> for c in g:
...   print(ord(c),end='')

84 104 105 115 32 105 115 32 97 10 116 101 115 116 105 110 103 
32 102 105 108 101 32 111 102 10 112 108 97 105 110 32 116 101 
120 116 46
```

Notice the 10 (0x0A). Windows uses CR/LF ... 0x0D + 0x0A. Linux and MAC ... just 0x0A.

Python has opened this file as text. It will process the line feeds for you. We'll see
binary in a moment.

Specifically, CP-1252 encoding on my windows machine:

```
>>> f
<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
# On raspberry pi
<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
```

More on encodings in a bit.

# Read a line at a time

```
f = open('test.txt')

g = f.readline()
print(g)
g = f.readline()
print(g)

g = f.read()
print(g)
f.close() # These will be closed when my program ends, but a good habit
```

Notice the LF on the end of the string. You can use `strip` to take it off.

You can for-each over the lines:

```
f = open('test.txt')
for g in f:
    print(g)
```

You can read all the lines into a list of strings:

```
f = open('test.txt')
g = f.readlines()
f.close()
print(g)
```

# Writing text files

```
f = open('out.txt','w')
f.write('hello\nworld\n')
f.close()
```

Note that the data isn't written to the disk until you close the file. Even `flush` doesn't send it.

# With

```
f = open('test.txt')
try:        
    f.read()        
finally:
    f.close()

##### INSTEAD DO THIS   
     
with open('test.txt') as f:
    f.read()
```

Easier to read. Doesn't work if the file outlives the section of code.

In Java, we have try-with-resources ... tied to the try/catch

# Binary files

```
>>> f = open('test.txt','rt')
>>> g = f.read()
>>> g
'This is a\ntesting file of\nplain text.'
>>> len(g)
37
>>> f.close()
>>> f = open('test.txt','rb')
>>> g = f.read()
>>> g
b'This is a\r\ntesting file of\r\nplain text.'
>>> len(g)
39
```

# Binary encoding

```
>>> g = 'baño' # Pasted characters from the web
>>> g
'baño'
>>> g.encode('utf-8')
b'ba\xc3\xb1o'
>>> g.encode('utf-16')
b'\xff\xfeb\x00a\x00\xf1\x00o\x00'
>>> g.encode('cp1252')
b'ba\xf1o'

# If I write as a text file, I get the cp1252 encoding by default on windows.
```

So, how do you want it written/read to/from disk? What format?

UTF-8 has been standardized as THE web encoding by HTML5.

Back and forth between strings and bytes -- for our English letters, one-character-equals-one-byte.

```
>>> g = 'baño'
>>> h = g.encode() # 'utf-8' is the default
>>> print(h)
# b'ba\xc3\xb1o'
>>> j = h.decode() # 'utf-8' is the default
>>> print(j)
# baño

# In case you are wrong
>>> i = h.decode('cp1252')
>>> i
'baÃ±o'

>>> i = h.decode('utf-16')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0x6f in position 4: truncated data
```

# Text representations

  - CR/LF used by HTTP protocol ... blank lines separate sections
  - XML is good at representing complex tree data, but a bit verbose
  - JSON complex trees ... less verbose ... directly to JS objects (used a lot on the web)

```
import json

d = {
    'name' : 'chris',
    'cool' : True,
    'snakes' : None,
    'favorites' : ['pizza',42,[1,2,3]]
}

g = json.dumps(d)
print(g)
```

```json
{"name": "chris", "cool": true, "snakes": null, "favorites": ["pizza", 42, [1, 2, 3]]}
```

```
c = json.loads(g)
print(c)
```

```python
{'name': 'chris', 'cool': True, 'snakes': None, 'favorites': ['pizza', 42, [1, 2, 3]]}
```

Doesn't work if you have cycles in the graph (loops of pointers).

# Misc things to know about files

  - You can open for appending and read/write
  - You can call `tell` to get your current position in the file (best for binary)
  - You can call `seek` to jump around in the file (best for binary)
  - Rich library of functions to list and traverse directories `os.listdir` and `os.isfile`

