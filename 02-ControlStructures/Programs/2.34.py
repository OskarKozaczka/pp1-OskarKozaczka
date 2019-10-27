
pesel=input("Podaj pesel: ")
x=pesel.isdigit()

while(x == False or len(str(pesel))!=11):
    pesel = input("Podaj pesel: ")
    
if(int(pesel[9])%2 == 1):
    print("Plec: mezczyzna")
else:
    print("Plec: kobieta")
    
if (int(pesel[2])>1):
    print("Wiek: " and 18-int(pesel[:2]))
else:
    print("Wiek" and 118-int(pesel[:2]))
          
    

