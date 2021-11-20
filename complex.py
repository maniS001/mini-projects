from time import *

def flyod():
  n=int(input('enter the value'))
  c=0
  for i in range(n):
    for j in range(i+1):
      c=c+1
      print(c,end=" ")
    print()




    
def pascalnew(n):
    h=0
    a=[1,1]

    for i in range(n):
      for k in range(n-i):
        print(end=" ")
      sleep(1)
       
      if h==0:
           print('1'.center(10))
          
      elif h==1:
            print(1,'',1)
      else:
                b=[1,1]
                for j in range(len(a)-1):
                    c=a[j]+a[j+1]
                    b.insert(j+1,c) 
                a=b
                for l in a: 
                    print(l ,end="  ")
                    
                print()
      h=h+1
      
    
def pascal():

        n=int(input('enter range'))
        print([1])
        a=[1,1]
        print(a)
        for j in range(n):
            i=0
            b=[1]
            while i<len(a)-1:
                c=a[i]+a[i+1]
                b.append(c)
                i=i+1
            b.append(1)
            a=b
            print(a)
def gcd():
    a=int(input('enter enter'))
    b=int(input('ennter 2'))
    d=0
    for i in range(1,max(a,b)):
      if a%i==0 and b%i==0:
        if i>d:
          d=i
        
    print(d)


pascalnew(10)




from threading import *
from time import *

def enc(st):
    x=st.encode()
    for i in x:
        print(i,end=" ")
        sleep(1)
def dec(st):
    for i in st:
        print(i)
        sleep(1)
p=Thread(target=enc,args=("mani8227",))
q=Thread(target=dec,args=("mani8227",))
p.start()
sleep(0.2)
q.start()
p.join()
q.join()
print('bye')
    
                




       
