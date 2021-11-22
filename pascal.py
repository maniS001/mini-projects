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


#another method
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
      
    





                

