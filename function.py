"""What is a function in Python?
In Python, a function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes the code reusable.

Syntax of Function
def function_name(parameters):
	#docstring
	statement(s)
Above shown is a function definition that consists of the following components.

Keyword def that marks the start of the function header.
A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
Parameters (arguments) through which we pass values to a function. They are optional.
A colon (:) to mark the end of the function header.
Optional documentation string (docstring) to describe what the function does.
One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
An optional return statement to return a value from the function."""

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul')