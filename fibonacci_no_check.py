#ayush gupta k 28
a=int(input("enter a number : "))
b=0
c=1
sum=0
while(sum<a):
    sum=c+b
    b=c
    c=sum
if(sum==a):
    print("yes")
else:
    print("no")
