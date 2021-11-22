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



