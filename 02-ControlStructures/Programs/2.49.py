nrDniaTygodnia=int(input('Nr dnia Tygodnia: '))

if nrDniaTygodnia<0 or nrDniaTygodnia>6:
    print("ERROR 404")
else:    
    




    print ('| PN | WT | SR | CZ | PT | SB | ND |')
    if nrDniaTygodnia>0:
        for x in range(nrDniaTygodnia):
            print('|   ', end =" ")
    
    for x in range(1,10):
        if (nrDniaTygodnia+x-1)==7 or (nrDniaTygodnia+x-1)==14:
            print('|')
        print('| ',x, end =" ")
    
    for x in range(10,31):
        if (nrDniaTygodnia+x-1)%7==0:
            print('|')
        print('|',x, end =" ")    
    
    for x in range (5-nrDniaTygodnia):
            print('|   ', end =" ")
    if nrDniaTygodnia!=6:
        print('|')
    else:
        for x in range (6):
            print('|   ', end =" ")
    
        print('|')
        
    
