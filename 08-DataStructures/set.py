set1 = {1,2,3,4,5}
set2 = set([2,4,6,8,10,12])


print(set1)
print(set2)

print(len(set2))

suma=0
for i in set1:
    suma+=i
print(suma)

print(set2-set1)
print(set2.difference(set1))

print(set1.intersection(set2))

for i in set1:
    if i ==6:
        print ("set1")
        
for i in set2:
    if i ==6:
        print ("set2")
        
set1.add(6)
set1.add(7)
set2.discard(12)

print(set1,set2)