class KT():
    
    
    def __init__(self,title,author,pages):
        
        self.title=title
        self.author=author
        self.pages=pages
        self.page=0
        self.IsOpened=False;
        
    def Open(self):
        self.IsOpened = True;
        
    def Close(self):
        self.IsOpened = False;
        
    def Status(self):
        print(self.title,self.author,self.pages,self.page)
        
    def ReadPage(self):
        if self.page<self.pages and self.IsOpened==True:
            self.page+=1
        if self.IsOpened==False:
            print("Zamkniętą książke czytasz??")
       
       
        
        
        