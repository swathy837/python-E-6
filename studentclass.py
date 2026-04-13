import sys
import gc

class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []

    class Student:
        def __init__(self, rollno, name, university):
            self.rollno = rollno
            self.name = name
            self.university = university

        def display_details(self):
            print("Roll No:", self.rollno, "Name:", self.name, "University:", self.university.university_name)

    def add_student(self, rollno, name):
        student = University.Student(rollno, name, self)
        self.students.append(student)
        print("Student added:", name)
        print("Reference count of student:", sys.getrefcount(student))

    def remove_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                print("Removing student:", student.name)
                print("Reference count before removal:", sys.getrefcount(student))

                self.students.remove(student)

                print("Reference count after removal:", sys.getrefcount(student))

                del student
                print("Garbage collected objects:", gc.collect())
                return

        print("Student not found")

    def display_all(self):
        if len(self.students) == 0:
            print("No students available")
        else:
            print("Students in", self.university_name)
            for student in self.students:
                student.display_details()


# Main program
gc.enable()

uname = input("Enter University Name: ")
u = University(uname)

while True:
    print("\n1.Add Student  2.Remove Student  3.Display All  4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        u.add_student(roll, name)

    elif choice == 2:
        roll = int(input("Enter Roll No to remove: "))
        u.remove_student(roll)

    elif choice == 3:
        u.display_all()

    elif choice == 4:
        print("Final garbage collection:", gc.collect())
        break

    else:
        print("Invalid choice")
