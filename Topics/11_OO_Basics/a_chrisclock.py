# Here is how I am keeping time: number of minutes
# since 6:00AM

minutes = 185.52

# What if I want to change to:

#secs = 11131.2

# Or

#hours = 3
#minutes = 5
#secs = 31
#msecs = 200


def get_seconds():
    return minutes * 60
    # return secs
    # return hours*60*60+minutes*60+secs+msecs/1000


# In fact, we want to hide the fact that there are "minutes". Not because it is a secret, but
# because we don't want users to use it accidentally. Other languages have a "private" keyword.
# Python ... you can't ENFORCE privacy. But the convention is to suggest
# it with a leading "_"

# _minutes = 185.52

# If you find yourself using functions or variables that begin with "_", you should
# check yourself.


# It is better to PROGRAM TO THE INTERFACE -- NOT THE IMPLEMENTATION
# Hide the data behind functions. This is called ENCAPSULATION

# Now the details about how time is stored is hidden. It is "private" user's
# don't need to know the secrets or tedious details. They just call public
# functions to get what they want.

# Design for flexibility.

# Cost: extra code to call the function (extra time)
# What if the code never changes? Wasted.

# Crystal Ball