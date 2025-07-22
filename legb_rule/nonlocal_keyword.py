# nonlocal_keyword.py

# The 'nonlocal' Keyword in Python
# The 'nonlocal' keyword allows you to modify variables from enclosing (but non-global) scopes

print("Understanding the 'nonlocal' Keyword in Python\n")

# 1. Nested Functions and Enclosing Scopes
def outer_function():
    x = 10  # Variable in the enclosing scope
    
    def inner_function():
        print(f"Accessing 'x' from enclosing scope: {x}")  # Can access but not modify
    
    inner_function()
    print(f"Value of 'x' after inner function: {x}")  # Still 10

print("1. Nested Functions and Enclosing Scopes:")
outer_function()
print()

# 2. Problem: Modifying Variables in Enclosing Scopes
def outer_function_problem():
    counter = 0  # Variable in the enclosing scope
    
    def inner_function_problem():
        # This creates a new local variable instead of modifying the enclosing one
        try:
            counter = counter + 1  # This will cause an error
            print(f"Counter: {counter}")
        except UnboundLocalError as e:
            print(f"Error: {e}")
            print("Explanation: Python sees 'counter' on the right side and assumes it's local,")
            print("but it hasn't been defined in the local scope yet.")
    
    inner_function_problem()
    print(f"Counter after inner function: {counter}")  # Still 0

print("2. Problem with Modifying Variables in Enclosing Scopes:")
outer_function_problem()
print()

# 3. Solution: Using the 'nonlocal' Keyword
def outer_function_solution():
    counter = 0  # Variable in the enclosing scope
    
    def inner_function_solution():
        nonlocal counter  # Declare that we want to use the enclosing 'counter'
        counter = counter + 1
        print(f"Counter inside inner function: {counter}")
    
    print(f"Counter before inner function: {counter}")
    inner_function_solution()
    print(f"Counter after inner function: {counter}")  # Now 1

print("3. Solution Using the 'nonlocal' Keyword:")
outer_function_solution()
print()

# 4. Multiple Nonlocal Variables
def outer_multiple():
    x = 10
    y = 20
    
    def inner_multiple():
        nonlocal x, y  # You can declare multiple nonlocal variables
        x = x * 2
        y = y * 3
        print(f"Inside inner function: x = {x}, y = {y}")
    
    print(f"Before inner function: x = {x}, y = {y}")
    inner_multiple()
    print(f"After inner function: x = {x}, y = {y}")

print("4. Multiple Nonlocal Variables:")
outer_multiple()
print()

# 5. Nested Scopes and Variable Resolution
def level1():
    a = 100
    
    def level2():
        b = 200
        
        def level3():
            nonlocal a  # Refers to 'a' from level1
            nonlocal b  # Refers to 'b' from level2
            a += 1
            b += 1
            print(f"Inside level3: a = {a}, b = {b}")
        
        print(f"Before level3: a = {a}, b = {b}")
        level3()
        print(f"After level3: a = {a}, b = {b}")
    
    print(f"Before level2: a = {a}")
    level2()
    print(f"After level2: a = {a}")

print("5. Nested Scopes and Variable Resolution:")
level1()
print()

# 6. Closures with Nonlocal Variables
def counter_factory():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment  # Return the inner function

print("6. Closures with Nonlocal Variables:")
counter1 = counter_factory()
counter2 = counter_factory()

print(f"Counter1 first call: {counter1()}")
print(f"Counter1 second call: {counter1()}")
print(f"Counter1 third call: {counter1()}")

print(f"Counter2 first call: {counter2()}")  # Each closure has its own 'count'
print()

# 7. Nonlocal vs. Global
x = "global"

def outer_scope():
    x = "enclosing"
    
    def inner_scope_nonlocal():
        nonlocal x
        x = "modified enclosing"
        print(f"Inner (nonlocal): {x}")
    
    def inner_scope_global():
        global x
        x = "modified global"
        print(f"Inner (global): {x}")
    
    print(f"Outer (before nonlocal): {x}")
    inner_scope_nonlocal()
    print(f"Outer (after nonlocal): {x}")
    
    print(f"Outer (before global): {x}")
    inner_scope_global()
    print(f"Outer (after global): {x}")  # Unchanged by global modification

print("7. Nonlocal vs. Global:")
print(f"Global (before): {x}")
outer_scope()
print(f"Global (after): {x}")
print()

# 8. Common Use Case: Memoization
def create_memoized_function():
    cache = {}  # Enclosing variable to store cached results
    
    def fibonacci(n):
        # Use cache to avoid recalculating values
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
        
        # Store result in cache
        cache[n] = result
        return result
    
    return fibonacci

print("8. Common Use Case: Memoization:")
fib = create_memoized_function()

import time
start = time.time()
print(f"Fibonacci(30): {fib(30)}")
end = time.time()
print(f"Time taken: {end - start:.6f} seconds")

# Without memoization, this would be much slower
print()

# End of examples