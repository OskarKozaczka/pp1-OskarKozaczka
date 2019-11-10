def jestImie(imie,imiona):
    
    x=0
    
    for i in range(len(imiona)):
        if imie==imiona[i]:
            x=1
            
    print("Imiona: ", end="")
    for i in range(len(imiona)):
        print(imiona[i],end=" ")
    print()
    print('Imie: ',imie)
    if x==1:
        
        print('Rezultat: imię zawarte jest w wykazie imion')
    else:
        print('Rezultat: imieni nie jest zawarte w wykazie imion')
    

    

imiona=['Janek','Ania','Wojtek','Zosia']

jestImie('Wojtek',imiona)