#ayush gupta k 28
n=int(input("enter a number of terms : "))
a=0
b=1
print("the fibonacci series of ",n," terms is :")
print(a,",",b,end="")
while(n>2):
    c=a+b
    print(",",c,end="")
    a=b
    b=c
    n=n-1
    
    
