"""The if…elif…else statement is used in Python for decision making.

Python if Statement Syntax
if test expression:
    statement(s)
Here, the program evaluates the test expression and will execute statement(s) only if the text expression is True.

If the text expression is False, the statement(s) is not executed."""
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
    print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
    print("This is also always printed.")
# Program checks if the number is positive or negative
# And displays an appropriate message
num = -1
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")