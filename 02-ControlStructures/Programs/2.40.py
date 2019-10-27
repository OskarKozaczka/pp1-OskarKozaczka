from random import randint
cyfry = ['jedynka', 'dwojka', 'trojka', 'czworka', 'piatka', 'szostka']
ilosc = [0, 0, 0, 0, 0, 0]

for i in range(100):
    x = randint(0,5)
    ilosc[x]+=1
    
for i in range(6):
    print(f"{cyfry[i]}: {ilosc[i]}")
    
    
    
    