# tuples_example.py

# 1. What is a Tuple?
# A tuple is a collection of ordered and immutable elements in Python.
# Tuples are often used to store related, fixed collections of data.

# Example of tuple creation
empty_tuple = ()
single_element_tuple = (42,)  # You must include a comma for a single-element tuple
multi_element_tuple = (1, 2, 3, 4, 5)

print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Multi-element tuple:", multi_element_tuple)

# 2. Accessing elements of a tuple
# Like lists, you can access tuple elements using indexing.
sample_tuple = ("apple", "banana", "cherry")
print("First element:", sample_tuple[0])
print("Last element:", sample_tuple[-1])

# 3. Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Element from nested tuple:", nested_tuple[1][0])  # Accessing a nested element

# 4. Tuple immutability
# Tuples are immutable, so their contents cannot be changed after creation.
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[1] = 99
except TypeError as e:
    print(f"Error: {e}")

# 5. Tuple unpacking
coordinates = (10, 20)
x, y = coordinates
print("x:", x, "y:", y)


# 6. Using tuples to return multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)


numbers = [3, 5, 2, 8, 1]
min_val, max_val = min_max(numbers)
print("Minimum:", min_val, "Maximum:", max_val)

# 7. Tuple methods
example_tuple = (1, 2, 3, 2, 2, 4)
print("Count of 2:", example_tuple.count(2))  # Count the occurrences of an element
print("Index of first occurrence of 3:", example_tuple.index(3))

# 8. Membership testing
languages = ("Python", "Java", "C++")
print("Is 'Python' in tuple?:", "Python" in languages)
print("Is 'Ruby' in tuple?:", "Ruby" not in languages)

# 9. Advantages of tuples
# Tuples are faster than lists because they are immutable.
# They can be used as keys in dictionaries (if they contain only immutable elements).
point = (1, 2)
point_dict = {point: "Coordinate 1"}
print("Dictionary with tuple as key:", point_dict)

# 10. Converting between tuples and other data types
list_example = [1, 2, 3]
tuple_from_list = tuple(list_example)
print("Tuple from list:", tuple_from_list)

tuple_example = (4, 5, 6)
list_from_tuple = list(tuple_example)
print("List from tuple:", list_from_tuple)

# End of examples