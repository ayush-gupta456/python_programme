#ayush gupta k 28
string=input("enter a string :")
a=""
for i in range(-1,-len(string)-1,-1):
    a=a+string[i]
print("reverse of string is : ",a)    
if a==string:
    print("string is a palindrome")  
else:
    print("string is not a palindrome")      