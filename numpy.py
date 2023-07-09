from numpy import *
als=[]
row1=int(input("enter the number of rows first matrix :"))
col1=int(input("enter the number of column first matrix :"))
for i in range(0,row1):
    ls1=[]
    for j in range(0,col1):
        y=eval(input("enter the value : "))
        ls1.append(y)
    als.append(ls1)
print(als)
row2=int(input("enter the number of rows second matrix :"))
col2=int(input("enter the number of column second matrix :"))
bls=[]
for i in range(0,row2):
    ls1=[]
    for j in range(0,col2):
        y=eval(input("enter the value : "))
        ls1.append(y)
    bls.append(ls1)
print(bls) 
if col1==row2:
    arr=dot(als,bls)
    print("the multiplication of two matrix is :")
    print(arr)