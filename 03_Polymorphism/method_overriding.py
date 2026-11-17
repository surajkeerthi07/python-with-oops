class Dog:
    def sound  (self):
        print("Dog sound")
    def eat(self):
        print("Dog eat")
class Cat(Dog):
    def sound  (self):
        print (" Cat sound")
c = Cat()
c.sound()
d = Dog ()
d.sound()
