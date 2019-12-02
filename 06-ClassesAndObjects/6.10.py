class TV():
    
    def __init__(self):
        
        self.is_on=False
        self.channel_no=1
        self.channels=[]
        
        
        
    def on(self):
        self.is_on=True
        
    def off(self):
        self.is_on=False
        
    def show_status(self):
        if (self.is_on==False):
            print(self.is_on)
        if (self.is_on==True and self.channels[self.channel_no-1]!=[]):
            print(self.is_on,self.channel_no,self.channels[self.channel_no+1])
            
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
        
    def set_channels(self,channels_list):
        self.channels=channels_list+self.channels  
    def show_channels(self):
        print (self.channels)
    
        
        
    
    
    
        
LG=TV()
LG.show_status()
LG.set_channel(5)
LG.on()
LG.show_status()
LG.off()
LG.show_status()
LG.set_channels(["TVP1","TVP2","Polsat","Filmbox"])
LG.show_channels()
LG.show_status()
LG.off()

