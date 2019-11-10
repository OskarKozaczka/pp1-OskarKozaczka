tab=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1]

def mediana(tab):
    tab.sort()
    
    if len(tab)%2==1:
        return tab[(len(tab)//2)]
    
    if len(tab)%2==0:
        return (tab[int(len(tab)/2-1)]+tab[int(len(tab)/2)])/2
    


def dominata(tab):
    tab.sort()
    x=''
    c=0
    cmax=0
    cliczba=''
    for i in range(len(tab)):
        if x==tab[i]:
            c+=1
        else:
            c=0
            
        if cmax<=c:
            cmax=c
            cliczba=tab[i]
        x=tab[i]

    return cliczba




print(mediana(tab))
print(dominata(tab))