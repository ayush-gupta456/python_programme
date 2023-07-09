'''unique 100 lottery numbers with two winners''' 
from random import *
from string import *
l=[]
count=0
print("The list of lotteries number are :")
for i in range(1,1000,1):
    a=choices(digits,k=10)
    b=''.join(a)
    if b not in l:
        l.append(b)
        print(i,": ",b)
        count=count+1
    if count==100:
        break
c=choices(l,k=2)
print("The first winner of lottery is : ",c[0])
print("The second winner of lottery is : ",c[1])
