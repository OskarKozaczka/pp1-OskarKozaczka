i=0
tab=[]
with open('../numbers.txt','r') as file:
    for line in file:
        tab.append(line)
        
        
        
tab.sort()


for i in range (0, len(tab)):
    print (tab[i], end="")
    