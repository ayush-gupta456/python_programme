#ayush gupta k 28
num=int(input("enter a number : "))
count=0
while(num>0):
    if num&1==1:
        count=count+1
    num=num>>1
print(count)        