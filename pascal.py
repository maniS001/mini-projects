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





                

