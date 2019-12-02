class University():
    
    def __init__(self):
        
        self.name = 'UEK'
        
        self.fullname = "Uniwersytet Ekonomiczny w Krakowie"
        
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
        
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname 
        
x=University()
x.set_name("AGH")
x.print_name()
x.print_fullname()
x.set_fullname("Akademia górniczo Hutnicza")
x.print_fullname()

