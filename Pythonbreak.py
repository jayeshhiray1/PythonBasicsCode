#Python break

# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

'''pass is just a placeholder for
functionality to be added later.
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would give an error. So, we use the pass statement to construct a body that does nothing.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass