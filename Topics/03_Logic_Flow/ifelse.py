def old():
    # Two kinds of jumps ... forwards (skip over code) and backwards (repeat code)
    
    # ## THINK PYTHON: CH5 Conditionals and Recursion
    
    # Forward skips are IF/ELIF/ELSE
    # Backward skips are loops WHILE/FOR
    
    a = 7
    
    print('start')
    
    if a==5:
        print('FIVE')
    elif a==6:
        print('SIX')
    elif a==7:
        print('SEVE')
    else:
        print('OTHER')
        
    print('done')
            
    # if a>=1 and a<=10:
    
    if a>5 and a<4:
        print('wow')
        
    if not a>5:
        print('pass')
        
    # These expressions are booleans
    
    # Logical operators
    # ==, !=, <, <=, >, >=
    
    x = a>5 # True or False
    
    if x:
        print('Pass')
    
    def is_it_five_forty():
        return True    
    if is_it_five_forty():
        print('DING DING DING')
        
    # Python will asses the "true-ness" of a value
    if 1:
        print('1 is True')
    
    if not 0:
        print('0 is False')
      
    s = 'j'  
    if s:
        print('non-empty string is True')
        
    s = ''
    if not s:
        print('empty string is False')
        

def one():
    
    if a==1:
        print('A')
    else:
        if a==2:
            print('B')
        else:
            print('C')
                
def two():
    
    if a==1:
        print('A')
    elif a==2:
        print('B')    
    else:
        print('C')
        
def three():
    a = 'hello' and [1,2,3]
    
def four():
    for i in range(20):
        print(i)
                
import dis

dis.dis(four)

#print('*****')
#dis.dis(one)
#print('*****')
#dis.dis(two)
    