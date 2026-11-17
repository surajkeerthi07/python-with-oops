# CRT Program 24: Getter method / retrieving object details

class Student:
    def __init__(self):
        self.name = "Rahul"
        self.age = 20

    def get_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student()
student.get_details()
