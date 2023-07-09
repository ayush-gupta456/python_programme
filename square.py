#ayush gupta k 28
a=int(input("enter a number of elements :"))
ls=[]
ls2=[]
sum=0
for i in range(0,a):
    ls.append(int(input()))
    sum=ls[i]*ls[i]
    ls2.append(sum)
print("the list is : ",ls,"  the square of the element of list 1 is : ",ls2)    
              
