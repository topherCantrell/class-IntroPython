# Strings

a = str() # An empty string
a = '' # An empty string
a = 'hello world'

print(len(a)) # 11

a = '''multi
line
string'''

a = 'hello\nthere\nworld'

ord('A') # 65 is the ascii code

chr(66) # 'B' is the ascii character

print(a[4]) # 'o' Negative indices also work

# Strings cannot be changed. These methods return NEW strings.

a = a.upper() # To upper case
a = a.lower() # To lower case
a = a.replace('hi','HEY') # replace all 'hi' with 'hey'

if 'he' in a:
    print('Found it')
    
i = a.index('lo') # Find 'lo' starting at 0
i = a.index('lo',5) # Find 'lo' starting at 5

a = 'hello world'
b = a[4:7] # 'o w'


