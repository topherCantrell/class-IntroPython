# Lists

p = ['hello','there','world']  # Creating a list
w = p[1]   # Accessing items (by index)
w = p[-1]  # Negative indecies start at the end

w[1] = 'THERE' # Changing items

p.append('!!!') # Appending items

p.insert(2,'The') # Inserting items

del p[0] # Removing (deleting) items

if 'there' in p: # Checking for an item
    print('The word "there" was found')
    
s = len(p) # Getting the number of items

for i in p: # Iterating over a list
    print(i) 
    
# Tuples

p = ('hello','there','world') # Just like lists ... but not mutable

p[1] = 'NOPE' # GENERATES AN ERROR
p.append('NOPE') # GENERATES AN ERROR

x = p[0] # Getting items

# Packing and unpacking (lists and tuples)

p = (1,2,3,4)
a,b,c,d = p # a=1, b=2, c=3, d=4

def fun():
    return 1,2,3,4 # Really returns a tuple with 4 things

a,b,c,d = fun() # Unpacks the 4 things from the tuple
