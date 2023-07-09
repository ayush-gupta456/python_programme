#ayush gupta k 28
num=int(input("enter a number : ")) 
a=""
b=""
tem=num
while(num>0):
    if (num&1==1):
        a="1"+a
        b=b+"1"
    else:
        a="0"+a
        b=b+"0"
    num=num>>1  
print("binary conversion of  %d  is : %s"%(tem,a))   
print("flip of binary conversion of  %d  is : %s"%(tem,b))  
        