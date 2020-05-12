
print ('I am here')

class Point:
    
    _num_created = 0
    
    print('Class loaded')
    
    
    def get_num_created():
        return Point._num_created
    
    def __init__(self):
        #self._num_created += 1
        Point._num_created += 1
        print(self._num_created)

print('HERE')
print(Point.get_num_created())
a = Point()
print(a._num_created)
print(a.get_num_created())
