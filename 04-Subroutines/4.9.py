def wystepuje(liczba,tab):
    
    x=0
    check=0
    print("Liczba: ",liczba)
    print("Tablica: ", end="")
    for i in range(len(tab)):
        x+=tab[i]
        if tab[i]==liczba:
            check=1
    
        print(tab[i]," ", end="")
    print("")
    if check==1:
        print("Rezultat: Podana liczba występuje w tablicy")
    else:
        ("Rezultat: Podana liczba nie występuje w tablicy")
    
        
            

tab=[15, 38, 7, 23, 14]

wystepuje(23,tab)