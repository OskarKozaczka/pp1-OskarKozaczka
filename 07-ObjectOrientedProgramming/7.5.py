class Music():
    
    def __init__(self, title,author,album,year):
        self.title = title
        self.author = author
        self.album = album
        self.year = year
        
    
    def __str__(self):
        return "Title: " + self.title +"\n"+"Author: " + self.author +"\n"+"album: " + self.album +"\n"+"Year: " + str(self.year)
                
    
m1 = Music('Nie ma Fal',"Podsiadło","Małomiasteczkowy",2018)
print(m1)      


m2 = Music('Nie ma Zaliczenia',"Cebo","Dużomiasteczkowy",2019)
print(m2)

m3 = Music('Są Fale',"Cebo i spółka","Cebo",2029)
print(m3) 