# CRT Program 15: Function demonstrating polymorphism
# One function works with different objects that provide an eat() method.

class Dog:
    def eat(self):
        print("Dog eats")


class Cat:
    def eat(self):
        print("Cat eats")


def food(animal):
    animal.eat()


dog = Dog()
cat = Cat()

food(dog)
food(cat)
