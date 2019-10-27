import random

rzut=random.randint(1,6)
guess=int(input("Zgadnij wyrzuconą liczbę oczek:"))
if guess==rzut:
    print("Zgadłeś!")
else:
    print("Komputer wyrzucił",rzut,"Spróbuj jeszcze raz!")