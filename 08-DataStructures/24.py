import json,re

Litery={}

with open('DontMakeMeWait.txt') as f:
    file=f.read()
  
  
for i in file:

    x=re.findall("[a-z]",i,flags=re.IGNORECASE)
    if len(x)==1:
        Litery[i.lower()]=0
    
    
for i in file:
    x=re.findall("[a-z]",i,flags=re.IGNORECASE)
    if len(x)==1:
        Litery[i.lower()]+=1
  

print(Litery.items())

with open("Litery.json","w") as file:
    json.dump(Litery,file,indent=4)