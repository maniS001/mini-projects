a=['mani','inam','san','main','','anm']
b=[]
l=len(a)
i=0
while i<l:
    c=[]
    c.append(a[i])
    for k in a[i+1:]:
        for j in a[i]:
            if j not in k:
                break
        else:
          c.append(k)
          a.remove(k)
    b.append(c)
    l=len(a)-1
    i+=1
print(b)
print(a)