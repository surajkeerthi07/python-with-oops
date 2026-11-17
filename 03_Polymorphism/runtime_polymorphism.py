# CRT Program 14: Runtime polymorphism through method overriding

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    # The method that runs depends on the object's actual type.
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
