#ayush gupta k 28
row=int(input("enter no of rows of pattern : "))
row-=1
i=1
while(row>=0):
    print(" "*row,"*"*i)
    row-=1
    i+=2