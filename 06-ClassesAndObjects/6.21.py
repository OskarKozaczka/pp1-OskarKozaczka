import statistics

class Statystyka():
    
    def __init__(self):
        self.tab=[]
        self.Max=0
        self.Min=0
        self.Mean=0
        self.Median=0
        
    def add(self):
        self.tab.append(int(input("Podaj Liczbe:")))
        
    def Show(self):
        for i in range(len(self.tab)):
            print(self.tab[i],end=" ")
        print("")
            
            
    def SetMax(self):
        self.Max=max(self.tab)
        
    def SetMin(self):
        self.Min=min(self.tab)
        
    def SetMean(self):
        self.Mean=statistics.mean(self.tab)
        
    def SetMedian(self):
        self.Median=statistics.median(self.tab)
        
    def Print(self):
        print(self.Min)
        print(self.Max)
        print(self.Mean)
        print(self.Median)
      
      
      
x=Statystyka()

x.add()
x.add()
x.add()
x.add()
x.add()
x.Show()
x.SetMin()
x.SetMax()
x.SetMean()
x.SetMedian()
x.Print()