tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

x=0

for i in range(len(tab)):
    if isinstance(tab[i],(int))==True:
        x+=tab[i]
    elif isinstance(tab[i],(list))==True:
        
        
        for r in range(len(tab[i])):
            if isinstance(tab[i][r],(int))==True:
                x+=tab[i][r]
            elif isinstance(tab[i],(list))==True:
                
                
                for g in range(len(tab[i][r])):
                    if isinstance(tab[i][r][g],(int))==True:
                        x+=tab[i][r][g]
                    elif isinstance(tab[i],(list))==True:
                        
                        
                        for b in range(len(tab[i][r][g])):
                            if isinstance(tab[i][r][g][b],(int))==True:
                                x+=tab[i][r][g][b]
