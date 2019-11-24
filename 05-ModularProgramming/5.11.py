import dane,obliczenia,wyniki

tekst=dane.czytajTekst("spendings.txt")

kwoty=dane.pobierzDane(tekst)

srednia=obliczenia.srednia(kwoty)
mediana=obliczenia.mediana(kwoty)
minimum=obliczenia.minimum(kwoty)
maximum=obliczenia.maximum(kwoty)

wyniki.pokazWyniki(kwoty,srednia,mediana,minimum,maximum)

wyniki.pokazWykres(kwoty)