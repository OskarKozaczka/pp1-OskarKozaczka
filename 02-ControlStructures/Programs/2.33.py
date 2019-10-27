liczby = ("zero",'jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec')
y = (input("Wprowadz liczbe: "))
x=len(str(y))
for i in range(x):
    cyfra = y[i]
    cyfra=int(cyfra)
    print(liczby[cyfra], end=" ")



    