import string
import random
from time import sleep
inp=int(input("Enter the Length of your Password\n"))
a=list(string.ascii_letters)
b=list(string.digits)
c=list(string.punctuation)
d=[]
d.extend(a)
d.extend(b)
d.extend(c)
random.shuffle(d)
sleep(1)
print("Your password of Length",inp,"is This")
print("".join(d[0:inp]))
