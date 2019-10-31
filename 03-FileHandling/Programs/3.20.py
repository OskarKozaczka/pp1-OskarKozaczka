tab=[]

with open('../numbers.txt', 'r') as file:
    for line in file:
        x=int(line)
            
        if x%2==0:
            tab.append(x)
             
with open('evennumbers.txt', 'w') as file:
    for i in range(0, len(tab)):
        file.write(str(tab[i])+" ")
    