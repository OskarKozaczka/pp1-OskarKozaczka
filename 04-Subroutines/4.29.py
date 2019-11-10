def sumaCyfr(n):
    
    if n<=9:
        return n
    

    if n>9:
         return n%10+sumaCyfr(n//10)

        





print(sumaCyfr(5839))