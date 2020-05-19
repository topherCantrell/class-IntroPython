

def a():
    f = open('test.txt')
    
    g = f.readline()
    print(g)
    g = f.readline()
    print(g)
    
    g = f.read()
    print(g)
    f.close()

def b():    
    f = open('test.txt')
    for g in f:
        print(g)
        
def c():
    f = open('test.txt')
    g = f.readlines()
    print(g)
    f.close()

def d():
    f = open('out.txt','w')
    f.write('hello\nworld\n')
    f.close()
    
def e():
    import json
    
    d = {
        'name' : 'chris',
        'cool' : True,
        'snakes' : None,
        'favorites' : ['pizza',42,[1,2,3]]
    }
    
    g = json.dumps(d)
    print(g)
    
    c = json.loads(g)
    print(c)
    
def w():
    f = open('test.txt')
    try:        
        f.read()        
    finally:
        f.close()
        
def w2():
    with open('test.txt') as f:
        f.read()
        
import dis

print(dis.dis(w))
print('---')
print(dis.dis(w2))