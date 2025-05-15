# Test case for the provided pattern-matching code

subject = [3.5, 7, 0]

# declarative
match subject:
    case list([int() | float() as x, int() | float() as y, 0]):
        print(f"declarative Point({x}, {y})")

# Test case for imperative pattern matching
if (
        isinstance(subject, list) and
        len(subject) == 3 and
        (isinstance(subject[0], (int, float))) and
        (isinstance(subject[1], (int, float))) and
        subject[2] == 0
):
    x, y = subject[0], subject[1]
    print(f"imperative Point({x}, {y})")
