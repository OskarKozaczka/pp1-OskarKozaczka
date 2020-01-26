import random

class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix
    
    @staticmethod
    def transpose(matrix):
        tab=matrix
        tab2=[]
        for i in range(len(tab[0])):
            
            row=[]
            for x in range(len(tab)):
                row.append(tab[x][i])
            tab2.append(row)

        return tab2
        
    @staticmethod
    def create2(y,x):
        return [[0 for x in range(x)] for y in range(y)] 


    @staticmethod
    def create_unit(x):
        tab=matrix.create(x,x)
        
        for i in range(x):
          
            tab[i][i]=1
        
        return tab
    
    @staticmethod
    def fill_random(matrix,m,n):
        tab=matrix
        
        for i in range(len(matrix)):
            
            for z in range(len(matrix[0])):
          
                tab[i][z]=random.randint(m,n)
        
        return tab
    
        

    
    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
            
    @staticmethod
    def create_diagonal(x,m,n):
        tab=matrix.create(x,x)
        
        for i in range(x):
          
            tab[i][i]=random.randint(m,n)
        return tab
    
    @staticmethod
    def compare(m1,m2):
        c=0
        if len(m1)<len(m2):
            x=len(m1)
        else:
            x=len(m2)
        
        for i in range(x):
            if m1[i]==m2[i]:
                c=1
        if c==1:
            return True
        else:
            return False
            


m = matrix.create2(4,3)
m2 = matrix.create2(4,3)
m3 = matrix.create2(4,3)
matrix.print(m)
print()
tab=matrix.create_unit(5)
matrix.print(tab)

m=matrix.fill_random(m,3,5)
print()
matrix.print(m)

m=matrix.transpose(m)
print()
matrix.print(m)
d= matrix.create_diagonal(5,1,2)
print()
matrix.print(d)

print()
matrix.print(m3)
print()
matrix.print(m2)
print(matrix.compare(d,m))
print(matrix.compare(m2,m3))

