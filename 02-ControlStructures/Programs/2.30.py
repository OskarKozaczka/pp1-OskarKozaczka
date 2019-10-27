pin = input("Podaj pin: ")

bool = 0

for i in range(2):
    if (pin=="0805"):
        print("Pin prawidłowy: ")
        break
        bool = 1
    else:
        print("Pin nieprawidłowy")
        pin = int(input("Podaj pin: "))
if (bool==0):
    print("Pin nieprawidlowy. Karta zablokowana")    
          