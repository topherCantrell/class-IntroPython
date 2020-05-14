# Dictionaries

d = {'name':'chris','age':25}

e = {
    'name': 'fred',
    'age': 30
}

d['age'] = 45     # Changing a value
d['cool'] = True  # Adding a mapping

a = d['age']      # Looking up a value

del d['cool']     # Deleting a mapping

if 'cool' in d:   # Check for a key
    print('yes')
    
for k in d:       # Iterate over keys
    print('key',k)
    
for k,v in d.items(): # Iterate over all mappings
    print('key=',k,'value=',v)
    
s = len(k) # Number of mappings

