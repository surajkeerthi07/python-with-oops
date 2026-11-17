# CRT Program 19: Public, protected and private attributes
# Python uses naming conventions and name mangling rather than strict
# access modifiers like some other languages.

class Animal:
    def __init__(self):
        self.name = "Dog"          # Public attribute
        self._type = "Mammal"      # Protected-by-convention attribute
        self.__species = "Canine"  # Private-by-name-mangling attribute

    def display(self):
        print("Public:", self.name)
        print("Protected:", self._type)
        print("Private (inside class):", self.__species)


animal = Animal()
animal.display()

# Public and protected attributes can be accessed from outside.
print("Outside - public:", animal.name)
print("Outside - protected:", animal._type)

# Private attribute is not accessed directly by its original name.
# Python name-mangles it to _Animal__species.
print("Outside - private via name mangling:", animal._Animal__species)
