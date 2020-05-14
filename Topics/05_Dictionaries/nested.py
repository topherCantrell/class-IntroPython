
'''
  0  1
  2  3
  4  5
'''

a = [
    [0,1],
    [2,3],
    [4,5]
    ]

print(a)

print(a[1][1]) # Row 1 column 1

a[1].append(100) # Now ragged

print(a)


b = {
    'name' : 'chris',
    'numbers' : [1,2,3,4]
}

print(b['numbers'][2])

c = {
    'name' : 'chris',
    'phones' : {
        'work' : 1234,
        'home' : 5678
    }
}

print(c['phones']['work'])