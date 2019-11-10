
def reverse(tab):
    tab2=[]
    for i in range(len(tab)):
        
        tab2.append(tab[len(tab)-i-1])
    

    return tab2




tab=[2, 5, 4, 1, 8, 7, 4, 0, 9]



print(reverse(tab))

