import statistics

with open('employees.csv','r') as file:
    age=[]
    for line in file:
        linesplited=line.split(',')
        if linesplited[2]!='age':
            age.append(int(linesplited[2]))
            



print(statistics.mean(age))
print(statistics.median(age))
print(statistics.pstdev(age))
