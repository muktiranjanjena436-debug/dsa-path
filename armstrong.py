# Armstrong number or not

n=int(input("enter the number:"))
num=n
total=0
ndigits=len(str(n))
while num>0:
    ld=num%10
    total=total+(ld**ndigits)
    num=num//10
print(total==n)