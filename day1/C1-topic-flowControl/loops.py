# ## THINK PYTHON: CH7 Iteration

# The WHILE loop is the most primitive. You must initialize the loop variable
# and you must change the loop variable as needed.

# BREAK looks back up to the first loop it finds and breaks out
# CONTINUE looks back up to the first loop it finds and continues

"""
x = 0
while x<5:
    print(x)
    x += 1
"""

"""
x = 0
while x<5:
    print('Top')
    x += 1
    if x==3:
        continue
    print(x)
"""

"""
x = 0
while x<5:
    print('Top')
    x += 1
    if x==3:
        break
    print(x)
"""