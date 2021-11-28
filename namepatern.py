a='manikandanmanikandanmanikandan'
n=5
g=0
m=n//2
print(m)
s=m
for c in range(5):
    g+=2

     
    if c%2==0:
        while c<len(a):
            print(a[c],end='   ')
            c+=n+m
        print()
    else:
        while c<len(a):
            print(a[c],end=' ')
            c+=s+g
       
        print()
#output
'''
m   m   h   l   i
o a a s a u h m d
h   d   h   a  
'''
