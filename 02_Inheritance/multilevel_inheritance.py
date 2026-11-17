# CRT Program 11: Multilevel inheritance

class Animal:
    def eat(self):
        print("Animal eats")


class Mammal(Animal):
    def sleep(self):
        print("Mammal sleeps")


class Dog(Mammal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.eat()
dog.sleep()
dog.sound()
