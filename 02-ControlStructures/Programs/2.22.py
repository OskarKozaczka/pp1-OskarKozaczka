tab=[15,8,31,47,2,19]

suma=0

n=len(tab)

for i in tab:
    if i%2==1:
        suma+=i
    else:
        n-=1
        
print(suma/n)