# pitfalls_and_best_practices.py

# Common Pitfalls and Best Practices with Python's LEGB Rule
# This script demonstrates common mistakes and recommended approaches

print("Common Pitfalls and Best Practices with Python's LEGB Rule\n")

# 1. Shadowing Built-in Functions
print("1. Shadowing Built-in Functions:")

# Bad practice: Shadowing built-in functions
def bad_shadowing_example():
    # Shadowing the built-in 'list' function
    list = [1, 2, 3]
    print(f"Local 'list' variable: {list}")
    
    try:
        # Now we can't use the built-in list() function
        new_list = list("abc")
        print(f"Converted string to list: {new_list}")
    except TypeError as e:
        print(f"Error: {e}")
        print("We can't use the built-in list() function anymore!")

# Good practice: Use different variable names
def good_naming_example():
    # Use a more descriptive name
    numbers_list = [1, 2, 3]
    print(f"Local 'numbers_list' variable: {numbers_list}")
    
    # We can still use the built-in list() function
    char_list = list("abc")
    print(f"Converted string to list: {char_list}")

bad_shadowing_example()
print()
good_naming_example()
print()

# 2. Forgetting that Default Arguments are Evaluated Only Once
print("2. Forgetting that Default Arguments are Evaluated Only Once:")

# Bad practice: Using mutable default arguments
def bad_default_args(name, items=[]):
    items.append(name)
    return items

print("Bad default arguments example:")
print(f"First call: {bad_default_args('Alice')}")
print(f"Second call: {bad_default_args('Bob')}")
print(f"Third call: {bad_default_args('Charlie')}")
print("Notice how the list keeps growing across calls!")

# Good practice: Use None as default and create the list inside the function
def good_default_args(name, items=None):
    if items is None:
        items = []
    items.append(name)
    return items

print("\nGood default arguments example:")
print(f"First call: {good_default_args('Alice')}")
print(f"Second call: {good_default_args('Bob')}")
print(f"Third call: {good_default_args('Charlie')}")
print()

# 3. Late Binding Closures
print("3. Late Binding Closures:")

# Bad practice: Using loop variables in closures
def bad_closure_example():
    functions = []
    for i in range(3):
        functions.append(lambda: i)
    return functions

bad_funcs = bad_closure_example()
print("Bad closure example:")
for f in bad_funcs:
    print(f"Function returns: {f()}")  # All will print the last value of i (2)

# Good practice: Capture the current value using default arguments
def good_closure_example():
    functions = []
    for i in range(3):
        functions.append(lambda i=i: i)  # i=i captures the current value
    return functions

good_funcs = good_closure_example()
print("\nGood closure example:")
for f in good_funcs:
    print(f"Function returns: {f()}")  # Each prints its own value
print()

# 4. Modifying Variables Across Scopes
print("4. Modifying Variables Across Scopes:")

# Bad practice: Relying heavily on global variables
counter = 0

def bad_increment():
    global counter
    counter += 1
    return counter

print("Bad practice (using global):")
print(f"First call: {bad_increment()}")
print(f"Second call: {bad_increment()}")
print(f"Global counter is now: {counter}")

# Good practice: Use parameters and return values
def good_increment(count):
    return count + 1

print("\nGood practice (using parameters):")
count = 0
count = good_increment(count)
print(f"After first call: {count}")
count = good_increment(count)
print(f"After second call: {count}")
print()

# 5. Overusing Nonlocal for Nested Functions
print("5. Overusing Nonlocal for Nested Functions:")

# Bad practice: Overusing nonlocal
def bad_nested_example():
    x = 10
    y = 20
    z = 30
    
    def inner_function():
        nonlocal x, y, z
        x += 1
        y += 1
        z += 1
        print(f"Inside inner: x={x}, y={y}, z={z}")
    
    inner_function()
    print(f"After inner: x={x}, y={y}, z={z}")

# Good practice: Be explicit about what you need
def good_nested_example():
    data = {'x': 10, 'y': 20, 'z': 30}  # Use a container
    
    def inner_function():
        # Only modify what you need
        data['x'] += 1
        return data['x']
    
    result = inner_function()
    print(f"Result from inner: {result}")
    print(f"After inner: {data}")

print("Bad nested example (overusing nonlocal):")
bad_nested_example()
print("\nGood nested example (using a container):")
good_nested_example()
print()

# 6. Unclear Variable Scope
print("6. Unclear Variable Scope:")

# Bad practice: Unclear where variables are defined
x = 100  # Global

def bad_scope_example():
    # Is this using the global x or creating a new local x?
    x = x + 1  # This will cause an error
    return x

# Good practice: Be explicit about scope
def good_scope_example():
    global x  # Explicitly state we're using the global x
    x = x + 1
    return x

print("Bad scope example:")
try:
    bad_scope_example()
except UnboundLocalError as e:
    print(f"Error: {e}")
    print("Python sees 'x' on the right side and assumes it's local,")
    print("but it hasn't been defined in the local scope yet.")

print("\nGood scope example:")
result = good_scope_example()
print(f"Result: {result}")
print(f"Global x is now: {x}")
print()

# 7. Excessive Nesting of Functions
print("7. Excessive Nesting of Functions:")

# Bad practice: Excessive nesting
def bad_nesting():
    a = 1
    
    def level1():
        b = 2
        
        def level2():
            c = 3
            
            def level3():
                d = 4
                nonlocal a, b, c
                return a + b + c + d
            
            return level3()
        
        return level2()
    
    return level1()

# Good practice: Flatten the structure
def good_structure(a=1, b=2, c=3, d=4):
    return a + b + c + d

print("Bad nesting example:")
print(f"Result: {bad_nesting()}")
print("\nGood structure example:")
print(f"Result: {good_structure()}")
print()

# 8. Using Class Attributes for Shared State
print("8. Using Class Attributes for Shared State:")

# Better alternative to global variables
class Counter:
    def __init__(self, initial=0):
        self.count = initial
    
    def increment(self):
        self.count += 1
        return self.count

print("Using class for shared state:")
counter = Counter()
print(f"Initial: {counter.count}")
print(f"After increment: {counter.increment()}")
print(f"After another increment: {counter.increment()}")

# Multiple instances don't interfere
counter2 = Counter(10)
print(f"Second counter: {counter2.count}")
print(f"After increment: {counter2.increment()}")
print()

# 9. Importing * Can Lead to Namespace Pollution
print("9. Importing * Can Lead to Namespace Pollution:")
print("Bad practice:")
print("from math import *  # Imports all names, can lead to unexpected shadowing")
print("\nGood practice:")
print("import math  # Then use math.sqrt(), math.pi, etc.")
print("from math import sqrt, pi  # Import only what you need")
print()

# 10. Summary of Best Practices
print("10. Summary of Best Practices:")
print("- Avoid shadowing built-in functions and types")
print("- Be careful with mutable default arguments")
print("- Be explicit about variable scope (use global/nonlocal when needed)")
print("- Prefer passing parameters and returning values over modifying outer scopes")
print("- Use classes for shared state instead of global variables")
print("- Keep function nesting to a reasonable level")
print("- Import only what you need, avoid 'import *'")
print("- Use descriptive variable names to avoid confusion")
print("- Document your code, especially when dealing with complex scoping")
print()

# End of examples