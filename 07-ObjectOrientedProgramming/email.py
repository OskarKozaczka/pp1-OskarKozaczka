from message import Message


class email(Message):
    
    
    def __init__(self,ad1,ad2,topic):
        
        self.ad1=ad1
        self.ad2=ad2
        self.topic=topic
        
    def send(self):
        
        print( self.ad1+"\n"+self.ad2+"\n"+self.topic+"\n" +self.message)