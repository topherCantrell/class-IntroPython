# Logic and Flow

# Simple IF
a = 7
if a == 7:
    print('It is seven')
    
# Simple IF/ELSE
if a == 7:
    print('It is seven')
else:
    print('Not seven')
    
# The ELIF
if a==1:
    print('One')
elif a==2:
    print('Two')
elif a==3:
    print('Three')
else:
    print('hummm')
    
# Complex expressions
if a<5 and a>2 and a!=2 and not a==3:
    print('yikes')
    
# Basic WHILE loop
x = 0
while x<5:
    print(x)
    x = x + 1
    
# Break and Continue
x = 0
while x<5:
    x = x + 1
    if x==2:
        break # Out of loop
    if x==3:
        continue # Back to the top
    
# Ranges
for i in range(10):
    print(i) # 0,1,2,3,4,5,6,7,8,9
    
for i in range(2,20,5):
    print(i) # 2 to 20 adding 5 each time