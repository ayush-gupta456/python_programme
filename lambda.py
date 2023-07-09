ls=[]
l=lambda x:ls.append(x)
ls1=['1',"2",'3','s']
for x in ls1:
     if (x.isnumeric()):
          l(x)
print(ls)
