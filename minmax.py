def fun(a):
    l=len(a)
    for i in range(l):
        if not i%2:
            for j in range(i+1,l):
                if a[i]<a[j]:
                    continue
                else:
                    a[i],a[j]=a[j],a[i]
        else:
            for j in range(i+1,l):
                if a[i]>a[j]:
                    continue
                else:
                    a[i],a[j]=a[j],a[i]
    return a
                   
print(fun([2,43,5,3,9,5,62,7]))