# CRT Program 4: Create multiple objects without a constructor

class Student:
    # Class attribute shared by instances unless overridden.
    name = "KPRIT"


student1 = Student()
student2 = Student()

print("Student 1:", student1.name)
print("Student 2:", student2.name)
