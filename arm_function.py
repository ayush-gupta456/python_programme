def arm(num):
    tem=num
    sum=0
    l=len(str(num))
    while(num>0):
        rem=num%10
        sum=sum+pow(rem,l)
        num=num//10
    if tem==sum:
        print(sum)
print("the list of armstrong number between 1 to 1000 are ")
for i in range(1,1000,1):
    arm(i)
