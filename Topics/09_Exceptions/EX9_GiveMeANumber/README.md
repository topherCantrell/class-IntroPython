# Give me a Number Between 1 and 100

Write a function to ask the user for a number from 1 to 100. This function should
only return an integer between 1 and 100. If you get anything else from the user,
provide an error message and loop back around to try again.

The `int()` function will raise an exception if the value is not numeric. Catch
this exception to provide an error message. 

Start with this code. Then fill out the `get_number` function.

```python
def get_number():
    pass
    
a = get_number()
print('You gave me',a)
```

Suggested output (be creative):

```
Give me a number between 1 and 100: -10
That is not between 1 and 100
Give me a number between 1 and 100: 500
That is not between 1 and 100
Give me a number between 1 and 100: elephant
That is not a number
Give me a number between 1 and 100: y8t7s
That is not a number
Give me a number between 1 and 100: 50
You gave me 50
```