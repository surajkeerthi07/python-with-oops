class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car brand:", self.brand)


c1 = Car("Toyota")
c2 = Car("BMW")

c1.show()
c2.show()
