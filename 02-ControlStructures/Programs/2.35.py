from math import sqrt
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))

delta = b**2-4*a*c
if (delta<0):
    print("Brak miejsc zerowych")
else:
    x1= (-b-sqrt(delta))/2*a
    x2= (-b+sqrt(delta))/2*a
    print(f"Miejsca zerowe to {x1} i {x2}") 
    

