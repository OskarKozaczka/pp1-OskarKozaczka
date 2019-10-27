a = int(input("Podaj ograniczenie predkosci: "))
b = int(input("Podaj predkosc: "))

if(b-a<10):
    mandat=(b-a)*5
else:
    mandat=(b-a-10)*15+50

print(f"Mandat (zl): {mandat}")
