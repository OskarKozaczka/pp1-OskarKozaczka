def suma(tab):
    
    x=0
    print("Tablica: ", end="")
    for i in range(len(tab)):
        x+=tab[i]
    
        print(tab[i]," ", end="")
    print("")
    print("Suma wartości:",x)
        
            

tab=[4,3,7,1,3]

suma(tab)