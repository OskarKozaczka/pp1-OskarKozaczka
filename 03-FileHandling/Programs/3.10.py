x=0
with open('../numbers.txt','r') as file:
    for line in file:
        line=int(line)
        x=x+line
print(x)        