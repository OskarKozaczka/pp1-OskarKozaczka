a = int(input("Wprowadz liczbe a: "))
b = int(input("Wprowadz liczbe b: "))
c = int(input("Wprowadz liczbe c: "))

if(a>b):
    temp = a
    a = b
    b = temp
if(b>c):
    temp = b
    b = c
    c = temp
if(a>b):
    temp = a
    a = b
    b = temp
    
print(f"{a} {b} {c}")