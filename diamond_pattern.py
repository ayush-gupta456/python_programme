#ayush gupta k 28
row=int(input("enter no of rows of pattern : "))
y=row*2-3
row-=1
i=1
while(row>=0):
    print(" "*row,"*"*i)
    row-=1
    i+=2
i=1
while(y>=0):
    print(" "*i,"*"*y)
    i+=1
    y-=2
