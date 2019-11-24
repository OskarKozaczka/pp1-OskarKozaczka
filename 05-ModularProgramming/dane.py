import re


def czytajTekst(nazwapliku):
    
    tekst=0

    with open(nazwapliku,'r') as file:
        for line in file:
            tekst=line
    return tekst  
        
def pobierzDane(tekst):

    kwoty= re.findall(r'\d{0,5}.\d{1,3} ',tekst)
    
    for i in range(len(kwoty)):
        kwoty[i]=float(kwoty[i])
        
    return kwoty

