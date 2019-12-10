class samolot():
    
    
    def __init__(self,numer):
        
        self.height=0
        self.numer=numer
        
        
    def SetHeight(self,height):
        
        if (height>300 and height<11000):
            self.height=height
        else:
            print("No nie bardzo")
            
    def Status(self):
        print(f"Tu {self.numer}, moja wysokość lotu to {self.height}m")
        
    def Start(self,x):
        if x>1000 and x<2000:
            self.height=x
        else:
            print("No nie bardzo")
            
    def Ląduj(self):
        if self.height<500:
            self.height=0
        else:
            print("Zbyt duża wysokość dla lądowania. Obniż lot")
            

Samolot=samolot("LOT881")
Samolot.Start(1400)
Samolot.Status()
Samolot.SetHeight(8900)
Samolot.Status()
Samolot.SetHeight(200)
Samolot.Status()
Samolot.Ląduj()
Samolot.Status()

