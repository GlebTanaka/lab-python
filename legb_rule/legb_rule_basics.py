# legb_rule_basics.py

# The LEGB Rule in Python
# LEGB stands for Local, Enclosing, Global, Built-in
# This rule defines the order in which Python looks up variable names

# 1. What is the LEGB Rule?
# The LEGB rule is Python's name resolution order for variable lookups.
# When you reference a variable in your code, Python searches for it in the following order:
# L - Local: Variables defined within the current function
# E - Enclosing: Variables defined in the enclosing function (for nested functions)
# G - Global: Variables defined at the top level of the module or declared global
# B - Built-in: Python's built-in names like print, len, etc.

print("LEGB Rule Demonstration\n")

# 2. Global Scope Example
x = 100  # This is a global variable

def test_global_scope():
    print(f"Accessing global 'x' from function: {x}")  # Python finds 'x' in the global scope

print("Global Scope Example:")
print(f"Global 'x': {x}")
test_global_scope()
print()

# 3. Local Scope Example
def test_local_scope():
    y = 200  # This is a local variable
    print(f"Local 'y': {y}")  # Python finds 'y' in the local scope
    
    # Trying to access local variable outside its scope will cause an error
    # Uncomment the next line to see the error:
    # print(f"Trying to access local 'y' outside function: {y}")

print("Local Scope Example:")
test_local_scope()
try:
    print(f"Trying to access local 'y' outside function: {y}")
except NameError as e:
    print(f"Error: {e}")
print()

# 4. Local vs Global Priority
x = 100  # Global variable

def test_local_priority():
    x = 200  # Local variable with same name as global
    print(f"Local 'x' inside function: {x}")  # Python uses the local 'x' (200)

print("Local vs Global Priority Example:")
print(f"Global 'x' before function call: {x}")  # 100
test_local_priority()  # Prints 200
print(f"Global 'x' after function call: {x}")  # Still 100, unchanged
print()

# 5. Enclosing Scope Example
def outer_function():
    z = 300  # Variable in the enclosing scope
    
    def inner_function():
        print(f"Accessing 'z' from enclosing scope: {z}")  # Python finds 'z' in the enclosing scope
    
    inner_function()

print("Enclosing Scope Example:")
outer_function()
print()

# 6. Complete LEGB Example
x = 100  # Global scope

def outer():
    x = 200  # Enclosing scope
    
    def inner():
        x = 300  # Local scope
        print(f"Local 'x' in inner(): {x}")
    
    inner()
    print(f"Enclosing 'x' in outer(): {x}")

print("Complete LEGB Example:")
outer()
print(f"Global 'x': {x}")
print()

# 7. Built-in Scope Example
# Built-in functions like print, len, etc. are in the built-in scope
print("Built-in Scope Example:")
print(f"Length of a list using built-in 'len()': {len([1, 2, 3, 4, 5])}")

# What if we define our own 'len'?
len = "This is not a function anymore!"
try:
    print(f"Length after redefining 'len': {len([1, 2, 3, 4, 5])}")
except TypeError as e:
    print(f"Error: {e}")

# Restore the built-in len
del len
print(f"Length after restoring built-in 'len': {len([1, 2, 3, 4, 5])}")
print()

# 8. Variable Shadowing
print("Variable Shadowing Example:")
animal = "Lion"  # Global

def zoo():
    animal = "Elephant"  # Shadows the global 'animal'
    print(f"Inside zoo() function: {animal}")

zoo()
print(f"In global scope: {animal}")
print()

# End of examples