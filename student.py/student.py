class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


student1 = Student("Arun", 21, 85)

student1.display_info()
