x=int(input("Podaj kwotę w zł: "))

tab1=[5,2,1]
tab2=[0,0,0]

i=0

print('Kwota' , x ,  'zł w monetach: ')

while x!=0:
    if x>=tab1[i]:
        x=x-tab1[i]
        tab2[i]+=1
    else:
        
        i+=1
        
 
for i in range(0,3):
    print(tab1[i],'zł - ' ,tab2[i],  'szt'  )  
    
    