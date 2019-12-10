import random
class Termometr():
    
    
    def __init__(self):
        
        self.IsOn=False
        self.temp=0
        
    def Zmierz(self):
        self.temp=random.randint(34,42)
        
    def Status(self):
        if self.IsOn==True:
            print(self.temp,end=" ")
            if self.temp>37:
                print("Gorączka",end=" ")
            if self.temp>41:
                print("Stan zagrożenia życia!!!")
        
    def On(self):
        self.IsOn=True
        
    def Off(self):
        self.IsOn=False
    
        


T=Termometr()

T.On()
T.Zmierz()
T.Status()
T.Off()

