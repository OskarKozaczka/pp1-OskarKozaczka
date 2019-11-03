import time

czas=time.time()

x=0


while x<90000000:
    x+=1

if x==90000000:
    czas2=time.time()
    
print ("dla while: ", (czas2-czas))




czas3=time.time()

x2=0


for i in range(90000000):
    x2+=1

    if x2==90000000:
        czas4=time.time()
    
print ("dla for: ", czas4-czas3)


print((czas2-czas)-(czas4-czas3))
