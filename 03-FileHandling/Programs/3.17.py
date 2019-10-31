import re

komunikat = 'To be, or not to be, that is the question'
samogłoski = re.findall('a',komunikat)
samogłoski = samogłoski + re.findall('o',komunikat)
samogłoski = samogłoski + re.findall('e',komunikat)
samogłoski = samogłoski +  re.findall('i',komunikat)

print(len(samogłoski))


