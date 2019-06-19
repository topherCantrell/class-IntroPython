# Save the Animals

Add a "save_zoo" function and a "load_zoo" function to the zoo.py module. These functions use the
hardcoded file name "zoo.json".

You will need to call these functions from the existing zoo.py module. Decide the best
place(s) to hook them in.

Snippet of code to convert a dictionary to a string:
```python
s = json.dumps(zoo)
```

Snippet of code to convert a string to a dictionary:
```
zoo = json.loads(s)
```