# CRT Program 22: Setter method

class Student:
    def __init__(self):
        self.name = "ABC"
        self.age = 35

    def set_details(self, name, age):
        self.name = name
        self.age = age


student = Student()
print("Before update:", student.name, student.age)

student.set_details("Mohan", 99)
print("After update:", student.name, student.age)
