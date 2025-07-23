# birds_v3.py - ABSTRACT BASE CLASSES BIRDS
from abc import ABC, abstractmethod


class Bird(ABC):
    """
    Abstract base class for birds.
    All bird types must implement the fly and swim methods.
    """
    @abstractmethod
    def fly(self):
        """Abstract method that all birds must implement."""
        pass

    @abstractmethod
    def swim(self):
        """Abstract method that all birds must implement."""
        pass


class Duck(Bird):
    def fly(self):
        print("Duck is flying at a moderate height.")

    def swim(self):
        print("Duck is swimming gracefully.")


class Swan(Bird):
    def fly(self):
        print("Swan is flying with long, smooth strokes.")

    def swim(self):
        print("Swan is gliding elegantly on the water.")


class Albatross(Bird):
    def fly(self):
        print("Albatross soars for hours without flapping its wings.")

    def swim(self):
        print("Albatross swims when necessary, though it prefers flying.")


# Example of what happens if you try to instantiate an abstract class
def demonstrate_abc_error():
    try:
        # This will raise TypeError because Bird is an abstract class
        bird = Bird()
        print("Created a Bird instance")
    except TypeError as e:
        print(f"Error: {e}")
    
    # This works because Duck implements all abstract methods
    duck = Duck()
    print("Created a Duck instance successfully")


# Example of what happens if you don't implement all abstract methods
class IncompleteImplementation(Bird):
    # Missing swim method implementation
    def fly(self):
        print("Flying but not swimming")


def demonstrate_incomplete_implementation():
    try:
        # This will raise TypeError because not all abstract methods are implemented
        incomplete = IncompleteImplementation()
        print("Created an IncompleteImplementation instance")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== ABC Error Demonstration ===")
    demonstrate_abc_error()
    print("\n=== Incomplete Implementation Demonstration ===")
    demonstrate_incomplete_implementation()