import math

c = 300000000  # Speed of light
# c = 3e8      # Python also support scientific notation

def get_moving_length(l0,v):
    # A moving object shrinks in the direction of travel.
    # This formula calculates the new length base on the
    # original length and the speed.
    d = 1 - (v*v) / (c*c)
    d = math.sqrt(d)
    # d = d**0.5 # This would have worked too ... without the math library
    return l0 * d

# Did you solve the equation to isolate v? That's the right
# way to do it.

# Here is another way: just try some values and narrow in on
# on a solution


#n = get_moving_length(12,100000000) # 11.3137 ... not fast enough
#n = get_moving_length(12,250000000) # 6.6332 Fits! But we can get closer to 10

n = get_moving_length(12,166000000) # 9.9955 Close enough for me

# Using the web to convert m/s to miles/hour:
# 230,734,650 miles/hour

print(n)

