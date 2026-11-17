# CRT Program 12: Multiple inheritance

class Father:
    def height(self):
        print("Father's height")


class Mother:
    def cook(self):
        print("Mother cooks")


class Child(Father, Mother):
    def study(self):
        print("Child is studying")


child = Child()
child.height()
child.cook()
child.study()
