import sys
import gc

class Student:

    class Course:
        def __init__(self, course_name):
            self.course_name = course_name

        def display_course(self):
            print("Course:", self.course_name)

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.courses = []

    def add_course(self, course_name):
        course = Student.Course(course_name)
        self.courses.append(course)

    def display(self):
        print("\nStudent Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Enrolled Courses:")
        for c in self.courses:
            c.display_course()


name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

s1 = Student(name, roll_no)

n = int(input("Enter number of courses: "))

for i in range(n):
    course_name = input("Enter course name: ")
    s1.add_course(course_name)

s1.display()

print("\nReference count:", sys.getrefcount(s1))

s2 = s1
print("After creating s2:", sys.getrefcount(s1))

del s2
print("After deleting s2:", sys.getrefcount(s1))

del s1

gc.collect()
print("Garbage collection completed")
