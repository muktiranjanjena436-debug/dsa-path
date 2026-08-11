# EXTRACTION OF DIGITS

num=5873
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
    print(num)
