def power(x,n):

    if  n==1:
        return x

    if n > 1:
        return x*power(x,n-1)
print(f'5 do potęgi 3 wynosi {power(5,3)}')