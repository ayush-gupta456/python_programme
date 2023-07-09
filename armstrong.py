#ayush gupta k 28
num=int(input("enter a number : "))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
if sum==temp:
    print(temp,"no. is armstrong")
else:
    print(temp,"no. not is armstrong")        






















































    