# This program is used to find the frequency of a number in a list and store it in a dictionary. 
# The time complexity of this program is O(n) and the space complexity is O(n).

#  method 1
frequency = {}
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
for i in range(0, len(num)):# time complexity=O(n) and space complexity=O(n)
    if num[i] in frequency:# time complexity=O(1) 
        frequency[num[i]] += 1# time complexity=O(1)
    else:
        frequency[num[i]] = 1# time complexity=O(1)
x = int(input("Enter the number to find its frequency: "))
print(frequency[x])

# method 2 

frequency = {}
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
for i in range(0, len(num)):
    frequency[num[i]] = frequency.get(num[i], 0) + 1
x=int(input("Enter the number to find its frequency: "))    
print(frequency[x])
