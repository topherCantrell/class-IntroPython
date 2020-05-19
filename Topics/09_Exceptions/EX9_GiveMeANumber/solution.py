def get_number():
    while True:
        r = input('Give me a number between 1 and 100: ')
        try:
            r = int(r)
            if r>=1 and r<=100:
                return r
            else:
                print('That is not between 1 and 100')
        except:
            print('That is not a number')                     
    
a = get_number()
print('You gave me',a)