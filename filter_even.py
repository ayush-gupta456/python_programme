ls=list(map(int,input("enter the , seperated values : ").split(",")))
ls1=list(filter(lambda a:True if a%2==0 else False,ls))
print(ls1)