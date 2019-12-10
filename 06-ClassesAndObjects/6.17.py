class fraction:
    
    
    def __init__(self):
        
        self.licznik=0
        self.mianownik=0
        
    def Create(self,licznik,mianownik):
        
        self.licznik=licznik
        self.mianownik=mianownik
        
    def Simplify(self):
        
        if self.mianownik%self.licznik==0:
            self.mianownik=int(self.mianownik/self.licznik)
            self.licznik=int(self.licznik/self.licznik)
    
    def Print(self):
        print(self.licznik,"/",self.mianownik)
        
        
        
Ułamek=fraction()

Ułamek.Create(1,2)
Ułamek.Print()

Ułamek.Create(12,21)
Ułamek.Print()

Ułamek.Create(2,4)
Ułamek.Simplify()
Ułamek.Print()