a=0
b=1
for i in range(1,20):
    '''
    print(a)
    c=a+b
    a=b
    b=c
    '''
    a,b=b,a+b
    print(a)
