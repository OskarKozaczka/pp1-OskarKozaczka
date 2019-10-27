x=int(input("Podaj Liczbę: "))


c=0
c2=0

threshold=2
    
    
while c2<x:    
    
    for i in range(1,threshold):
        if threshold%i==0:
            c+=1

    if c==1:
        print (threshold)
        c2+=1
    threshold+=1
    c=0

