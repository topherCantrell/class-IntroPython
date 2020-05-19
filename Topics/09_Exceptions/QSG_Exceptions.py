# Exceptions

raise KeyError('Some info')  # Raise an exception at any time

try:
    print('Do stuff')
    # raise KeyError
    print('Other stuff')
except KeyError: # Specific types of exceptions
    pass
    # Can use 'raise' here to re-raise the original exception
except ZeroDivisionError:
    pass
except Exception: # This catches most everything
    pass
#except: # Allowed, but frowned upon
#   pass
else: # Funs if an exception did NOT happen
    print('Did not get an exception')
finally:
    print('No matter what')
    