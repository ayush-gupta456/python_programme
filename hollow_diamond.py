#ayush gupta k 28
row=int(input("enter no of row : "))
row=row-1
print("*"*(2*row+2))
i=0
while(row>=1):
    print("*"*row," "*i,"*"*row)
    row=row-1
    i=i+2