
def find_average(data):
    sum = 0                 # I'll add them up here
    for i in data:          # For each item, one at a time in "i"
        sum = sum + i       # Add to the running sum
    return sum / len(data)  # Return the sum divided by the number of items


def count_target_items(data,target_item):
    ct = 0                   # To start with, I haven't found any
    for i in data:           # For each item, one at a time in "i"
        if i == target_item: # Does this item match the target item?
            ct += 1          # Yes ... bump the count
    return ct                # Return the count

# Simple test data here. I put in some duplicate 3s
test_data = [1,6,3,3,8,2,6,8,9]

# I did the average by hand (well, calculator). Should be 5.1111111
av = find_average(test_data)

# I see two 3's in the test data. Better be "2" reported here
ct = count_target_items(test_data,3)

print(av)
print(ct)

# Interestingly, the count_target_items only calls "==" on the objects.
# Any object that can answer "==" will work, and most all do.

# My test data here has lots of different kinds of things in it. As long as they
# can all "==" then my count function will work.
more_data = ['hello','hello','world',True,1,2,3]

# I see two 'hello' in the data. Better be a "2" reported here
ct = count_target_items(more_data,'hello')

print(ct)

