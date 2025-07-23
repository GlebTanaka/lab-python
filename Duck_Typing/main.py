# main.py - COMMON DRIVER CODE
from birds_v1 import Duck as InheritanceDuck, Swan as InheritanceSwan, Albatross as InheritanceAlbatross
from birds_v2 import Duck as DuckTypingDuck, Swan as DuckTypingSwan, Albatross as DuckTypingAlbatross
from birds_v3 import Duck as ABCDuck, Swan as ABCSwan, Albatross as ABCAlbatross


def test_birds(bird_classes):
    for BirdClass in bird_classes:
        bird = BirdClass()
        bird.fly()
        bird.swim()


def main():
    print("=== Inheritance Birds ===")
    test_birds([InheritanceDuck, InheritanceSwan, InheritanceAlbatross])
    print("\n=== Duck Typing Birds ===")
    test_birds([DuckTypingDuck, DuckTypingSwan, DuckTypingAlbatross])
    print("\n=== Abstract Base Class Birds ===")
    test_birds([ABCDuck, ABCSwan, ABCAlbatross])
    
    # Demonstrate ABC-specific features
    print("\n=== ABC Features Demonstration ===")
    import birds_v3
    birds_v3.demonstrate_abc_error()
    print()
    birds_v3.demonstrate_incomplete_implementation()


if __name__ == "__main__":
    main()