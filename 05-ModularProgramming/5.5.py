import statistics,re


wyn='21600 zł (wynagrodzenie prezesa ), 4350 zł, 3920 zł, 5590 zł, 3250 zł, 4010 zł'

wynagrodzenie=re.findall('[0-9]{4,5}', wyn)

for i in range (0, len(wynagrodzenie)):
    wynagrodzenie[i]=int(wynagrodzenie[i])




print ("mediana:",statistics.median(wynagrodzenie))
print ("srednia:",statistics.mean(wynagrodzenie))
print ("odchylenie:",statistics.pstdev(wynagrodzenie))

