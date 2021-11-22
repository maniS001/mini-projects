#to find floid triangle
from time import *
def flyod():
  n=int(input('enter the value'))
  c=0
  for i in range(n):
    for j in range(i+1):
      c=c+1
      print(c,end=" ")
    print()
#output : 
'''1
   2 3
   4 5 6
   7 8 9 10 '''




    
def pascalnew(n):
    h=0
    a=[1,1]

    for i in range(n):
      for k in range(n-i):
        print(end=" ")
      if h==0:
           print(1)
          
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




def name_pattern():
  a='mohamadshahulhamid'
  c=0
  while c<len(a):
      print(a[c],end='   ')
      c=c+4
  print()
  i=1
  while i<len(a):
      print(a[i],end=' ')
      i+=2
  print()
  c=2
  while c<len(a):
      print(a[c],end='   ')
      c=c+4
#output
'''m   m   h   l   i
o a a s a u h m d
h   d   h   a
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: max_areast[int]
        :rtype: int
        """
        self.height=height
        myList=self.height
        max_areas=[]
        for i in range(0,len(myList)):
            area=0
            for j in range(i):
                mini=min(myList[i],myList[j])
                p=(i-j)*mini
                if p>area:
                    area=p
            max_areas.append(area)
        return(max(max_areas))
obj=Solution()
print(obj.maxArea([32,5,6,7,5,6]))
#output:
'''find largest area between two lines
by ploting each value at graph
out: 30

'''
 
           
    

                




       
