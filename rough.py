import random
from copy import deepcopy
r=4
l=4
e=0
c=0
b=[]
a=[[random.randint(0,20) for i in range(l) ] for j in range(r)]
t=deepcopy(r*l)
while e<=t:
    back=False
    for i in range(r):
        if i==c:
            for j in range(l):
                b.append(a[i][j])
                e+=1
        elif i<r-1 and i!=c:
            b.append(a[i][l-1])
            e+=1
        else:
            c=0
            for j in range(l):
                c-=1
                b.append(a[i][c])
                e+=1 
            back= True 
            c=c+1
            r=r-2 
            l=l-1
        if back==True:
            pass
            


                 
print(a)
print(b)

            




     
            

        
    

    


