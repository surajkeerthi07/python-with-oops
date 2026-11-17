# CRT Program 5: Rectangle area and cuboid volume

class Rectangle:
    def area(self, length, breadth):
        print("Area:", length * breadth)

    def volume(self, length, breadth, height):
        print("Volume:", length * breadth * height)


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))

rectangle = Rectangle()
rectangle.area(length, breadth)
rectangle.volume(length, breadth, height)
