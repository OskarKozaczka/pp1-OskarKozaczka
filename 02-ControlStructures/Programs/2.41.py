x = int(input("Wprowadz liczbe, 0 = koniec: "))

suma = 0
ilosc = 0

while(x!=0):
    suma+=x
    ilosc+=1
    x = int(input("Wprowadz liczbe: "))
else:
    srednia = suma/ilosc
print(f"Rezultat: Liczb={ilosc}   Suma={suma}    Srednia={srednia}")
    
        
        