import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)


print((int(cyfry[0])+int(cyfry[1])+int(cyfry[2]))/3)