import random

class Kostka():
    
    def __init__(self):
        self.Oczka=0
        
        
    def Rzut(self):
        self.Oczka=random.randint(1,6)

    
    def Print(self):
        print(self.Oczka)
       
    
    def Ile(self):
        return self.Oczka
for i in range(5):
    
    Kostka1=Kostka()
    Kostka2=Kostka()
    Kostka3=Kostka()

    Kostka1.Rzut()
    Kostka1.Print()

    Kostka2.Rzut()
    Kostka2.Print()

    Kostka3.Rzut()
    Kostka3.Print()

    print(Kostka1.Ile()+Kostka2.Ile()+Kostka3.Ile())
    

