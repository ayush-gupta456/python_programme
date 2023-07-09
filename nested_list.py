ls=[]
row=int(input("enter the number of rows :"))
col=int(input("enter the number of column :"))
for i in range(0,row):
    ls1=[]
    for j in range(0,col):
        y=eval(input("enter the value : "))
        ls1.append(y)
        ls.append(ls1)
print(ls)        
