#ayush gupta k 28
num=int(input("entre a number : "))
sum=0
tem=num
while(num>0):
    rem=num%10
    sum=sum*10+rem
    num//=10
print("reverse of number %d is : %d"%(tem,sum))    