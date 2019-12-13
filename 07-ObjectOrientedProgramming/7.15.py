class book():
    
    
    def read(self):
        print("czytanko")

    

        
class ebook(book):
    
    def __init__(self,st):
        
        self.st=st
    
    
    
class regularbook(book):
    
    def __init__(self,file):
        
        self.file=file
        
        
Book1=ebook("book.exe")
Book2=regularbook(19)
Book2.read()