

def fib(n):
    
    if n==0:
        return 0
    
    if n==1:
        return 1
    
    if n>1:
        return int(fib(n-2))+int(fib(n-1))


        




for i in range(20):
    print(fib(i))