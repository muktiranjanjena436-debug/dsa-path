# hashing functions in python

#prestoring values into data structures.then fatching it

# method 1: 

x=[1,2,3,4,5,6,7,8,9]
y=[9,111,5,76,21,34,56,78,90]
for i in range(len(y)):
    count=0
    for j in range(len(x)):
            if y[i]==x[j]:
                count+=1
    print(f"Frequency of {y[i]} in list x is {count}")

# method 2 : using hash_list

x=[1,2,3,4,5,6,7,8,9]
y=[9,111,5,76,21,34,56,78,90]
hash_list = [0]*11
for i in x:
    hash_list[i] += 1
for i in y:
    if i<1 or i>10:
        print(f"Frequency of {i} in list x is 0")
    else:
        print(f"Frequency of {i} in list x is {hash_list[i]}")

# method 3: using dictionary

x=[1,2,3,4,5,6,7,8,9]
y=[9,111,5,76,21,34,56,78,90]
frequency = {}
for i in x:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
for i in y:
    if i in frequency:
        print(f"Frequency of {i} in list x is {frequency[i]}")
    else:
        print(f"Frequency of {i} in list x is 0")