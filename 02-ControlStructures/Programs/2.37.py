from statistics import median

a=int(input("Podaj liczbe a: "))
b=int(input("Podaj liczbe b: "))
c=int(input("Podaj liczbe c: "))

x=median([a,b,c])
print(f"Mediana: {x}")