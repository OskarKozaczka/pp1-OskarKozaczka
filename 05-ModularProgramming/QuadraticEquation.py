import math

#odczytaj współczynniki z klawiatury, zwraca tablicę współczynników
#czytajWspolczynniki() => float[a,b,c]

def czytajWspolczynniki():
    a=float(input('1: '))
    b=float(input('2: '))
    c=float(input('3: '))
    wsp=[a,b,c]
    
    return wsp


# oblicz deltę
#obliczDelte([a,b,c]) => float

def obliczDelte(wsp):

    return pow(wsp[1],2)-4*wsp[0]*wsp[2]




# wyznacz pierwiastki równania - zwraca tablicę pierwiastków (jeden lub dwa elementy) lub pustą tablicę, jeśli delta < 0
#obliczPierwiastki([a,b,c]) => float[x1,x2]

def obliczPierwiastki(wsp):
    pier=[]
    if obliczDelte(wsp)<0:
        return []
    if obliczDelte(wsp)==0:
        pier[0]=-wsp[1]/wsp[0]*2
        return pier
    
    if obliczDelte(wsp)>0:

        pier.append((-1*wsp[1]+math.sqrt(obliczDelte(wsp)))/(wsp[0]*2))
        pier.append((-1*wsp[1]-math.sqrt(obliczDelte(wsp)))/(wsp[0]*2))
        
        return pier


# wyświetl wyznaczone pierwiastki równania kwadratowego
#wyswietlPierwiastki([x1,x2])




def wyswietlPierwiastki(pier):
    if len(pier)==0:
        print("Nie ma pierwiastków")
    if len(pier)>0:
        print("x1:",pier[0])
    if len(pier)>1:
        print("x2:",pier[1])
    


