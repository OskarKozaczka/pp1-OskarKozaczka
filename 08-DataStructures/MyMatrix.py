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
            


m = matrix.create(4,3)
matrix.print(m)
print()
tab=matrix.create_unit(5)
matrix.print(tab)
print()
matrix.fill_random(m,3,5)
matrix.print(m)
