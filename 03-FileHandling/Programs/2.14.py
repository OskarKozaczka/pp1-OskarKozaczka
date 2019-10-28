tab=[32,16,5,8,24,7]

for i in range(0,len(tab)):

    with open('tablica cyferek.txt','a') as file:

            file.write(str(tab[i])+"\n")