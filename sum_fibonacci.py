#ayush gupta k 28
n=int(input("enter a number of term to be find of fibanacci series : "))
a=0
b=1
while(n>2):
    c=a+b
    a=b
    b=c
    n=n-1
print("the required term is : ",c)    
