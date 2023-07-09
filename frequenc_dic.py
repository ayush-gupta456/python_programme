#to count the frequency of the words
s=input("enter a string : ")
ls=list(s)
fre={}
for i in ls:
    if(i in fre):
        fre[i]+=1
    else:
        fre[i]=1
print(fre)