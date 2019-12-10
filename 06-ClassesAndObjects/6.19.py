class Rachunek():
    
    
    def __init__(self,numer):
        
        self.numer=numer
        self.saldo=0
        
    def wpłać(self,kwota):
        self.saldo+=kwota
        
    def wypłać(self,kwota):
        
        if self.saldo>=kwota:
            self.saldo-=kwota
            
        else:
            print ("Nie ma pieniędzy :(")
            
            
    def status(self):
        print(self.saldo)
        
Rachunek=Rachunek(12345655559090111100007722)
Rachunek.status()
Rachunek.wpłać(25.30)
Rachunek.status()
Rachunek.wypłać(31.70)
Rachunek.status()
Rachunek.wypłać(14)
Rachunek.status()
    