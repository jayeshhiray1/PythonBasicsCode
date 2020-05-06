def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

#user defined function
def add_numbers(x,y):
   sum = x + y
   return sum
#Global vs. Local variables
num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print("Outside the function global total : ", total)