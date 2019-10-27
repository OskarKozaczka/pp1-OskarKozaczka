nr=input("nr?: ")

x=0
    
if len(nr)!=26:
    print ('nr nie ma 26 cyfr')
else:
    for i in range(6):
    
            if x==0:
                print ("Nr rachunku: " , nr[0:2], end=" ")
            else:
                print (nr[x:x+4], end=" ")
    
    
            x=x+4
    


      
      
