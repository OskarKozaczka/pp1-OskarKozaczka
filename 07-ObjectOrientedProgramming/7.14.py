class mobile():
    
    
    def __init__(self,brand,ram,disp):
        
        self.brand=brand
        self.ram=ram
        self.disp=disp
        
    def Vibrate(self):
            
            print("vibrated")
            
    def call(self,nr):
            
            print ("calling: "+str(nr))
            
            
Tel1=mobile("samsung",4,"18:9")
Tel2=mobile("xiaomi",8,"21:9")

Tel1.call(1244)
Tel2.Vibrate()
        
        
    