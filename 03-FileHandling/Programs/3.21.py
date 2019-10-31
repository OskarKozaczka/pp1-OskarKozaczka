suma=0
counter= 0
x=[]

with open('../numbersinrows.txt', 'r') as file:
    for line in file:
        x=line.split(',')
        for i in range(0, len(x)):
            counter+=1
            suma+=int(x[i])
            
            
print(suma)
print(counter)