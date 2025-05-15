# birds_v2.py - DUCK TYPING BIRDS
class Bird:
    def fly(self):
        print("A bird is flying.")

    def swim(self):
        print("Some birds can swim.")


class Duck(Bird):
    def fly(self):
        print("Duck is flying, but stays near the water surface.")

    def swim(self):
        print("Duck swims smoothly in the pond.")


class Swan(Bird):
    def fly(self):
        print("Swan is flying elegantly with long wings.")

    def swim(self):
        print("Swan glides gracefully on the water.")


class Albatross(Bird):
    def fly(self):
        print("Albatross soars for long distances over the ocean.")

    def swim(self):
        print("Albatross swims occasionally, but prefers flying.")