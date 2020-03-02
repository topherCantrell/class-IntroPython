def add_two(a,b):
    print("Adding",a,b) # multiple things on a line
    c = a + b
    return c

x = add_two(1,2)
y = add_two(3,x)

# Could substitute in:

y = add_two(3, add_two(1,2))
print(y)

z = add_two(add_two(1,2),add_two(3,add_two(4,5)))
print(z)

# The computer calls the functions as needed to make the arguments to
# call the other functions. It starts left to right. Show the print.

# Do you like this compact expression? Or do you like to separate the
# steps out into local variables?