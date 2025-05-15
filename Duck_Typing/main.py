# main.py - COMMON DRIVER CODE
from birds_v1 import Duck as InheritanceDuck, Swan as InheritanceSwan, Albatross as InheritanceAlbatross
from birds_v2 import Duck as DuckTypingDuck, Swan as DuckTypingSwan, Albatross as DuckTypingAlbatross


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


if __name__ == "__main__":
    main()