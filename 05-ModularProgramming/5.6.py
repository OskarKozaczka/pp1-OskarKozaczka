import csv,statistics

c=0
i=1
wiek=[]
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if c>1:
            wiek.append(int(row[2]))
        
        c+=1
        
        if c==1:
            print('# SURNAME NAME AGE EMAIL')
            print('========================================================')
            
        if c>1:
            print(i,end=' ')
            for d in range(0,len(row)):
                 print(row[d],end=' ')
            print('')
            i+=1
        
print('średnia wieku: ',statistics.mean(wiek))