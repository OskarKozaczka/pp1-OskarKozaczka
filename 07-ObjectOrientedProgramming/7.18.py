

class Wypozyczalnia():
    
    
    def __init__(self,nazwa):
        
        self.lista=[]
        self.nazwa=nazwa
        
    def dodaj(self,x):
        
        self.lista.append(x)
        
        
    def Status(self):
        print(self.name)
      
    def Lista(self):
        
        for i in range(len(self.lista)):
            print(i+1,self.lista[i])
        print()
            
    def ListaWolne(self):
        
        for i in range(len(self.lista)):
            if self.lista[i].wyp=="nie":
                print(i+1,self.lista[i])
        print()
    def ListaZaj(self):
        
        for i in range(len(self.lista)):
            if self.lista[i].wyp=="tak":
                print(i+1,self.lista[i])
        print()     
    def zmien(self,nr):
        
 
        for i in self.lista:
            
            if i.nr==nr:
        
                if i.wyp=="nie":
                    i.wyp="tak"
                elif i.wyp=="tak":
                    KM=input("KM: ")
                    i.przebieg+=int(KM)
                    i.wyp="nie"



class vechicle():
    
    
    def __init__(self,marka,nr):
        
        self.marka=marka
        self.nr=nr
        self.przebieg=0
        self.wyp="nie"
        
    def __str__(self):
        
        return self.marka+" "+self.nr+" "+self.przebieg+" "+self.wyp
    
    def SetPrzebieg(self,x):
        self.przebieg=x
        
    def SetWyp(self,x):
        self.wyp=x
        
        
class Osobowy(vechicle):
    
    def __init__(self,marka,nr,miejsca):
        
        self.miejsca=miejsca
        super().__init__(marka,nr)
    
    def __str__(self):
        return self.marka+" "+str(self.nr)+" "+str(self.miejsca)
    
class Dostawczy(vechicle):
    
    def __init__(self, marka, nr,tony):
        
        
        self.tony=tony
        super().__init__(marka,nr)
        
        
    def __str__(self):
        return self.marka+" "+str(self.nr)+" "+str(self.tony)
    
    
Cebo=Wypozyczalnia("Cebo")

Cebo.dodaj(Osobowy("beta",44141,4))
Cebo.dodaj(Osobowy("audica",32141,4))
Cebo.dodaj(Osobowy("Mitsubishi",44151,2))
Cebo.dodaj(Dostawczy("Stilo",42411,2))
Cebo.dodaj(Dostawczy("IVECO",34141,7))

Cebo.Lista()

Cebo.zmien(32141)
Cebo.zmien(34141)

Cebo.ListaZaj()
Cebo.ListaWolne()

Cebo.zmien(32141)

Cebo.ListaZaj()
Cebo.ListaWolne()
