class Student():
    
    LastIndex=100000
    
    def __init__(self,name,lastname,subject):
        
        self.name=name
        self.lastname=lastname
        Student.LastIndex+=1
        self.index=Student.LastIndex
        self.subject=subject
        
       
        
    def __str__(self):
        return self.lastname+" "+str(self.index)+" "+self.subject+" Uek Kraków"
    
    
    
Cebo=Student("Cebo","Jakub","Informatyka Stosowana")
print(Cebo)

Wacław=Student("Wacław","POTOCKI","Informatyka Stosowana")
print(Wacław)

Jakub=Student("Jakub","Cebo","Informatyka Stosowana")
print(Jakub)