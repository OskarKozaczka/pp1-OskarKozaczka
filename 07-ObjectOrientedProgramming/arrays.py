import random

class arrays():
    

    sep=","
        
    @staticmethod  
    def sepc(x):
        arrays.sep=x
    
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
            
    @staticmethod
    def print_in_line(array):
        a=0
        for c in array:
            if a==0:
                print(c,end="")
                a+=1
            else:
                print(arrays.sep+str(c),end="")
                
    @staticmethod
    def new(ile,liczba):
        tab=[]
        for x in range(ile):
            tab.append(liczba)
        return tab
    
    @staticmethod
    def newr(ile,liczba,liczba2):
        tab=[]
        for x in range(ile):
            tab.append(random.randint(liczba,liczba2))
        return tab
            
            
    @staticmethod
    def sp(tab,od,do):
        c=0
        for x in tab:
            
            if x>od and x<do:
                c+=1
        print (c)

                
my_array = [4,1,8,7,2]
arrays.sepc("X")
arrays.print_in_line(my_array)