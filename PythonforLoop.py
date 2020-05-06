#Python for Loop
#Syntax of for Loop
"""for val in sequence:
	Body of for
Here, val is the variable that takes the value of the item inside the sequence on each iteration"""

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)

#The range() function

print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))
#for loop with else

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")