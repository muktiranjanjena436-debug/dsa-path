# COUNTING NUMBER OF DIGITS

n=int(input("enter the number:"))
num=len(str(n))
print(num)    

# method 2

n=5873
num=n

count=0
while num>0:
    count+=1
    num=num//10
print(count)

# method 3

import math
n=int(input("enter the number:"))
print(math.floor(math.log10(n))+1)