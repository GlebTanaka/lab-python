from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def process_color(color):
    match color:
        case Color.RED:
            print("It's red!")
        case Color.GREEN:
            print("It's green!")
        case Color.BLUE:
            print("It's blue!")
        case _:
            print("Unknown color")

process_color(Color.RED)   # Output: It's red!
process_color(Color.GREEN) # Output: It's green!