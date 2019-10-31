c=0
i=0
tab=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]


with open('3.24.txt', 'w') as file:
    for c in range(0,len(tab)):
        if c>0:
            file.write("\n")
        for i in range(0, len(tab)):
            file.write(tab[c][i]+" ")
    

                       
        
        

        
            
            

