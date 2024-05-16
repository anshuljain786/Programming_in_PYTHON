# Function Arguments
''' 
1. Default Arguments
 Functions can have default parameter values. If a value for a parameter is 
 not provided during the function call, the default value is used.

 '''
def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message
print(greet("Geeks"))

'''
2. Keyword Arguments
Passing keyword arguments allow the caller to specify the argument name with 
values so that the caller does not need to remember the order of parameters.

'''
def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
student(firstname='Python', lastname='Programmer')
student(lastname='Programmer', firstname='Python')

'''
3. Variable-length Arguments
Python supports variable-length arguments through *args and **kwargs. 
This allows a function to accept a flexible number of arguments.

'''

def print_values(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_values(1, 2, 3, name="Rose", age=24)

'''
Nested function
In Python, a nested function is a function defined inside another function. 
The inner function has access to the variables of the outer (enclosing) function, and it can use them even after the outer function has finished execution. This concept is known as "closure".

'''

def func_1(x):
    S = "Data Science with Python"
    def func_2():
        return (S,x)
    return func_2()

# Create a closure
closure = func_1(3.0)

print(closure)

'''
Recursive function
A recursive function is a function that calls itself either directly or 
indirectly in order to solve a problem. Recursive functions are useful for solving problems that can be broken down into smaller, similar sub-problems.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result) 
