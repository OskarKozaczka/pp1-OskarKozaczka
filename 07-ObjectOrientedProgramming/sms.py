from message import Message

class sms(Message):
    
    
    def __init__(self,tel1,tel2):
        
        self.tel1=tel1
        self.tel2=tel2
        
        
    def send(self):
        
        print( str(self.tel1)+"\n"+str(self.tel2)+"\n"+self.message)