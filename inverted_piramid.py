#ayush gupta k 28
row=int(input("enter no of rows of pattern : "))
row=row*2-1
i=0
while(row>=0):
    print(" "*i,"*"*row)
    i=i+1
    row=row-2