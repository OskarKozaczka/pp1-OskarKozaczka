def podatek(dochod):
    
    if dochod<=5000:
        return 0.17*dochod
    else:
        return 0.17*dochod+0.32*(dochod-5000)

dochod=int(input('Podaj dochod: '))
print('dochod należny:',int(podatek(dochod)),'zł')