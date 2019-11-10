import re

tekst = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
a = re.findall('a',tekst)
o = re.findall('o',tekst)
e = re.findall('e',tekst)
i = re.findall('i',tekst)
ą = re.findall('ą',tekst)

print('a =',len(a))
print('o =',len(o))
print('e =',len(e))
print('i =',len(i))
print('ą =',len(ą))