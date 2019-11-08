def suma(N):

    if  N==1:
        return 1

    if N > 1:
        return N + suma(N-1)
print(suma(500))