jezyki=['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci=[61,47,37,32,26,18,14,14,9,7]


  
  
def rysujWykres(jezyki,wartosci):
    for i in range(len(jezyki)):
        print(jezyki[i],':',end='')
        
        for x in range(10-len(jezyki[i])):
            print(' ',end='')
        
        for i in range(wartosci[i]):
            print('#',end='')
        print()



rysujWykres(jezyki,wartosci)