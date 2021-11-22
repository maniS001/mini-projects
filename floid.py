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
'''1s
   2 3
   4 5 6
   7 8 9 10 '''