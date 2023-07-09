from random import *
from string import *
p=[]
p=p+choices(digits,k=1)
p=p+choices(punctuation,k=1)
p=p+choices(ascii_uppercase,k=2)
p=p+choices(ascii_lowercase,k=6)
shuffle(p)
print("(the automatic generated password is) ",''.join(p))
