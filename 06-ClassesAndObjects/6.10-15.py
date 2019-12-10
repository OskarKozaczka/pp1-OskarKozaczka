class TV():
    
    def __init__(self):
        
        self.is_on=False
        self.channel_no=1
        self.channels=[]
        self.volume=0;
        
        
        
    def on(self):
        self.is_on=True
        
    def off(self):
        self.is_on=False
        
    def show_status(self):
        if (self.is_on==False):
            print(self.is_on)
        if (self.is_on==True and self.channels[self.channel_no-1]):
            print(self.is_on,self.channel_no,self.channels[self.channel_no-1],self.volume)

            
            
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
        
    def set_channels(self,channels_list):
        self.channels=channels_list+self.channels  
    def show_channels(self):
        print (self.channels)
        
        
    def volume_up(self):
        if self.volume<10:
            self.volume+=1
            
    def volume_down(self):
        if self.volume>0:
            self.volume-=1

        
LG=TV()
LG.show_status()
LG.set_channels(["TVP1","TVP2","Polsat","Filmbox"])
LG.set_channel(2)
LG.on()
LG.volume_up()
LG.volume_up()
LG.volume_up()
LG.volume_up()
LG.show_status()
LG.off()
LG.volume_down()
LG.volume_down()
LG.volume_down()
LG.volume_down()
LG.volume_down()
LG.volume_down()
LG.show_status()
LG.show_channels()
LG.show_status()
LG.on()
LG.set_channel(4)
LG.show_status()
LG.off()

