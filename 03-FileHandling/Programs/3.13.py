tab=[31,16,5,8,24,7]


for i in range(0, 6):
    with open('3.13.txt','a') as file:
        file.write(str(tab[i])+"\n")