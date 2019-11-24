def wspak(tekst):
    tekst2=[]
    for i in range(len(tekst)):
        
        tekst2.append(tekst[len(tekst)-i-1])   

    return ''.join(tekst2)

    



def rozstrzel(tekst):
    tekst2=[]
    for i in range(len(tekst)):
        
        tekst2.append(tekst[i])   

    return " ".join(tekst2)


def WlkLit(tekst):
    
        return tekst.title()


