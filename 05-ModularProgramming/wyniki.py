
def pokazWyniki(kwoty,srednia,mediana,minimum,maksimum):
    
    print("RAPORT Z WYDATKÓW")
    print("")
    print("MIESIĄC    WYDATKI")
    print("styczeń   ",kwoty[0])
    print("luty      ",kwoty[1])
    print("marzec    ",kwoty[2])
    print("kwiecień  ",kwoty[3])
    print("maj       ",kwoty[4])
    print("czerwiec  ",kwoty[5])
    
    print("")
    
    print("STATYSTYKA WYDATKÓW")
    print("średnia    ",srednia)
    print("mediana    ",mediana)
    print("minimum    ",minimum)
    print("maksimum   ",maksimum)
    print("")
    
def pokazWykres(kwoty):
    print("GRAFICZNA REPREZENTACJA WYDATKÓW")
    print("styczeń   ",round(kwoty[0]/100)*'#')
    print("luty      ",round(kwoty[1]/100)*'#')
    print("marzec    ",round(kwoty[2]/100)*'#')
    print("kwiecień  ",round(kwoty[3]/100)*'#')
    print("maj       ",round(kwoty[4]/100)*'#')
    print("czerwiec  ",round(kwoty[5]/100)*'#')
    
    
    