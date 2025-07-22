# global_keyword.py

# The 'global' Keyword in Python
# The 'global' keyword allows you to modify global variables from within functions

print("Understanding the 'global' Keyword in Python\n")

# 1. Problem: Modifying Global Variables from Functions
counter = 0  # Global variable

def increment_counter_wrong():
    # This creates a new local variable instead of modifying the global one
    counter = counter + 1  # This will cause an error
    return counter

print("1. Problem with Modifying Global Variables:")
try:
    increment_counter_wrong()
except UnboundLocalError as e:
    print(f"Error: {e}")
    print("Explanation: Python sees 'counter' on the right side and assumes it's local,")
    print("but it hasn't been defined in the local scope yet.")
print()

# 2. Solution: Using the 'global' Keyword
counter = 0  # Global variable

def increment_counter_correct():
    global counter  # Declare that we want to use the global 'counter'
    counter = counter + 1
    return counter

print("2. Solution Using the 'global' Keyword:")
print(f"Initial counter value: {counter}")
increment_counter_correct()
print(f"After first increment: {counter}")
increment_counter_correct()
print(f"After second increment: {counter}")
print()

# 3. Multiple Global Variables
x = 10
y = 20

def update_globals():
    global x, y  # You can declare multiple global variables
    x = x * 2
    y = y * 3
    print(f"Inside function: x = {x}, y = {y}")

print("3. Multiple Global Variables:")
print(f"Before function call: x = {x}, y = {y}")
update_globals()
print(f"After function call: x = {x}, y = {y}")
print()

# 4. Global Variables in Different Modules
print("4. Global Variables in Different Modules:")
print("When importing variables from other modules, they are already global in your module.")
print("You don't need the 'global' keyword to access them, only to modify them.")
print()

# 5. Best Practices with Global Variables
print("5. Best Practices with Global Variables:")
print("- Minimize the use of global variables when possible")
print("- Use global variables for constants (uppercase by convention)")
print("- Consider using classes or function parameters instead")
print("- Document your global variables clearly")
print()

# 6. Global Constants Example
PI = 3.14159  # Global constant (uppercase by convention)
GRAVITY = 9.8

def calculate_circle_area(radius):
    # No need for 'global PI' since we're only reading it, not modifying it
    return PI * radius * radius

def calculate_falling_distance(time):
    # No need for 'global GRAVITY' since we're only reading it, not modifying it
    return 0.5 * GRAVITY * time * time

print("6. Global Constants Example:")
print(f"Circle area with radius 5: {calculate_circle_area(5):.2f}")
print(f"Falling distance after 3 seconds: {calculate_falling_distance(3):.2f} meters")
print()

# 7. Avoiding Globals with Return Values
count = 0

def bad_increment():
    global count
    count += 1
    
def good_increment(value):
    return value + 1

print("7. Avoiding Globals with Return Values:")
print("Bad approach (using global):")
print(f"Initial count: {count}")
bad_increment()
print(f"After bad_increment(): {count}")

print("\nGood approach (using return values):")
count = good_increment(count)
print(f"After good_increment(): {count}")
print()

# 8. Global vs. Local Name Conflict
name = "Global"

def demonstrate_conflict():
    # This creates a local 'name' variable
    name = "Local"
    print(f"Local name: {name}")
    
    # To access the global 'name' variable, we would need 'global name'
    # But we can't use 'global name' after already using 'name' as local

def demonstrate_global_first():
    global name
    print(f"Global name (before change): {name}")
    name = "Modified Global"
    print(f"Global name (after change): {name}")

print("8. Global vs. Local Name Conflict:")
demonstrate_conflict()
print(f"Global name (unchanged): {name}")
demonstrate_global_first()
print(f"Global name (changed): {name}")
print()

# End of examples