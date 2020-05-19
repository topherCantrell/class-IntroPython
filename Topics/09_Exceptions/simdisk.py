def read_byte():
    print('Reading a byte')
    a = 0
    # If you wanted to return a code, what would it be?
    #raise Exception('disk error')
    print('Got the byte')
    return a

def read_word():
    print('Reading a word')
    a = read_byte()
    b = read_byte()
    print('Got the word')
    return a*256 + b

def read_long():
    print('Reading a long')
    a = read_word()
    b = read_word()
    print('Got the long')
    return a*65536+b

a = read_long()
print(a)

def basic():
    print('starting')
    
    try:
        print('I am here')
        b = [1,2,3]
        #a = 10/0 # ZeroDivisionError
        #a = crazy # NameError    
        #a = b[100] # IndexError
        #a = b.alkdsfjlaskdfj() # AttributeError
        print('And here')
    #except:
    #    print('First')
    except NameError:
        print('Got a name error')
    except IndexError:
        print('Got an index error')
    except:
        print('Something bad happened')
        
    print('finishing up')

