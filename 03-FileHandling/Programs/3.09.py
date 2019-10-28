
x=0
with open('../NoEducation.txt','r') as file:
    for line in file:
        print(f"{x}. {line}", end='')
        x+=1
