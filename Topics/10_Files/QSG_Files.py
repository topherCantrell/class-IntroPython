# Files

f = open('test.txt') # Open for reading (text)

f.read() # Read all

f.readline() # Read next line

for line in f: # Line by line
    print(line) 
    
f.close()

# Better to use 'with'

with open('test.txt') as f:
    pass

f = open('out.txt','w') # Again, use the "with" syntax
f.write('hello\nworld\n')
f.close()

# Bytes and Strings

a = 'hello'
x = a.encode() # to bytes
y = x.decode() # from bytes
