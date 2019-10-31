import re

cyfry=[]

with open('../land.txt', 'r') as file:
    for line in file:
        cyfry+= re.findall('\d',line)
        
print(len(cyfry))
        
            
            

