from math import sqrt
n = int(input("Wprowadz liczbe n: "))
liczby = [2,3]

kandydat=int(liczby[2:])+1
for i in range(10):
    for j in range(len(liczby)):
        while(liczby[j]<=sqrt(kandydat)):
            if(kandydat%liczby[i]==0):
                liczby.append(kandydat)
        