a=0
b=1
i=0
num=int(input("enter the number of terms : "))
print("the fibonacci series is :",a,end='')
f=lambda a,b:a+b
while (num>1):
    num=num-1
    a=b
    b=i
    print(",",f(a,b),end='')
    i=a+b