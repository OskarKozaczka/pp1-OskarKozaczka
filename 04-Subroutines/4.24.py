import random

def los():
    #print(random.randrange(1,51))
    return random.randrange(1,51)



parz=0
nparz=0
for i in range(1000):
    if los()%2==0:
        parz+=1
    else:
        nparz+=1
    
print('Dla 1000 liczb losowych z przedziału <1,50>:')
print('Liczby parzyste:',parz/10,'%')
print('Liczby nieparzyste',nparz/10,'%')