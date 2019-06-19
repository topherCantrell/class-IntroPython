
def read_byte(f):
    print('Reading a byte')
    return 0

def read_word(f):
    print('Reading a word')
    a = read_byte(f)
    b = read_byte(f)
    return a*256 + b

def read_long(f):
    print('Reading a long')
    a = read_word(f)
    b = read_word(f)
    return a*65536+b

f = None
a = read_long(f)
print(a)