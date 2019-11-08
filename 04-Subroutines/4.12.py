import random

def rzucKostka():
    x=random.randrange(1,7)
    return x

x1=rzucKostka()
x2=rzucKostka()
x3=rzucKostka()


print("Wyrzucone oczka: ",x1,x2,x3)
print("Suma oczek: ",x1+x2+x3)