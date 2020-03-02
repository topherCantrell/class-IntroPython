def say_hi():
    print("Hello")
    # Return is automatically added
    return

def add_two(a,b):
    c = a + b
    # This is how you return a value
    return c

say_hi()

x = add_two(3,4) # Return value is copied into x
print(x)

y = add_two(x,x)
print(y)
