
data = 'asdfasdfjlkjalsdfjwerltkjscflkjasdflkjweqrtlkasdfjlkasjdf'

def count_items(d):
    ret = {}
    for i in d:
        ret[i] = 0
    for i in d:
        ret[i] = ret[i] + 1
        
    ret = {}
    for i in d:
        if i in ret:
            ret[i] += 1
        else:
            ret[i] = 1
        
    return ret
        
r = count_items(data)
print(r)

r = count_items(['hello','there','world','hello','hello'])
print(r)

r = count_items([1,2,2,1,6,5,8,6,1])
print(r)

r = count_items([True,'hello',1,1,'hello',True])
print(r)
