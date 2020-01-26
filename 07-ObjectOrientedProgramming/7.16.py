from operator import attrgetter

class Student():
    
    
    def __init__(self,name,lastname,nr):
        
        self.name=name
        self.lastname=lastname
        self.nr=nr
        
    def __eg__(self,other):
        return self.nr==other.nr
    
    def __it__(self,other):
        return self.nr<=other.nr
    
    def __str__(self):
        
        return self.name+self.lastname+str(self.nr)
        
S1=Student("Anna ","Tomaszewska ",141820)
S2=Student("Wojciech ","Zbych ",201003)
S3=Student("Maja ","Kowalska ",153202)
S4=Student("Marek ","Migiel ",138600)

List=[S1,S2,S3,S4]


for i in List:
    print (i)
    
print()
#List=sorted(List,key=lambda x: x.nr, reverse=True)


List=sorted(List, key=attrgetter('nr'))

for i in List:
    print (i)