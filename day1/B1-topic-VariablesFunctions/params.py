def add_two(a,b):
    # local variables a and b are created here
    # the incoming values are COPIED to the locals
    c = a + b
    print(c)
    a = 2 # Doesn't affect the caller
    b = 4
    
a = 7
b = 8
add_two(a,b)

add_two(10,20)
