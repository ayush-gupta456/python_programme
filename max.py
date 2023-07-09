#ayush gupta k 28
a=int(input("enter a number of elements :"))
ls=[]
sum=0
for i in range(0,a):
    ls.append(int(input()))
print(ls)    
max=ls[0]
for i in ls:
    if max<i:
        max=i
print("max term is : ",max)        
        
