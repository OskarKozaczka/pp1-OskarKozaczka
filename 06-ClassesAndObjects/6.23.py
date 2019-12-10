class Kontakt():
    
    def __init__(self,nazwa,email,telefon):
        
        self.nazwa=nazwa
        self.email=email
        self.telefon=telefon
        
class ListaKontaktow():
    
    def __init__(self):
        
        self.Lista=[]
    
    
    
    def Nowy(self,kontakt):
        #kontakt=Kontakt()
        self.Lista.append(kontakt)
        
    def Status(self):
        
        for i in range(len(self.Lista)):
            print(self.Lista[i].nazwa,self.Lista[i].email,self.Lista[i].telefon)
            


ListaK=ListaKontaktow()

ListaK.Nowy(Kontakt("Kowalski Jan", "jank@onet.pl", "555234000"))
ListaK.Nowy(Kontakt("Borek Patrycja", "bp@o2.pl", "232000199"))
ListaK.Nowy(Kontakt("Maj Piotr", "maj@google.pl" ,"222999100"))
ListaK.Nowy(Kontakt("Adamczyk Anna", "ada@poczta.pl", "100200300"))
ListaK.Status()


