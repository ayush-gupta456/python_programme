file=open("ayush.txt","r")
ayush=file.read()
words=ayush.split()
count=0
li=0
for i in ayush:
    if i==" ":
        count=count+1
        li=li+1
print("the number of words in a file are :",len(words))
print("the number of alphabets in a file are :",len(ayush)-1-count)
print("the number of lines in a file are :",li)
