class Student:

    def __init__(self, name, age, course, class, marks):
        self.name = name
        self.age = age
        self.course = course
        self.class = class
        self.marks = marks
        

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Class:", self.class)
        print("Marks:", self.marks)


student1 = Student("Arun", 21, "Computer Science", "A", 85)

student1.display_info()
