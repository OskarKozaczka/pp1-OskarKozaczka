list=[]
i=0

with open('universities.txt', 'r') as file:
    for line in file:
        list.append(line)

list.sort()


        
        
with open('universities.txt', 'w') as file:
    for i in range(0, len(list)):
        file.write(list[i])
    
        
