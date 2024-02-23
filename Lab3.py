import math
import numpy as np

def round_down_score(score):
    return math.floor(score * 10) / 10

def calculate_average_gpa(credits, marks):
    total_credits = np.sum(credits)
    weighted_sum = np.sum(credits * marks)
    average_gpa = weighted_sum / total_credits
    return round(average_gpa, 2)

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def enter_marks(self, course_id, mark):
        rounded_mark = round_down_score(mark)
        self.marks[course_id] = rounded_mark

    def show_marks(self, courses):
        print(f"\nMarks for student {self.id}:")
        for course_id, course_data in courses.items():
            mark = self.marks.get(course_id)
            if mark is not None:
                print(f"Course {course_id}, Name: {course_data.name}: {mark}")
            else:
                print(f"Course {course_id}, Name: {course_data.name}: Marks not available")

    def calculate_gpa(self, courses):
        credits = []
        marks = []
        for course_id, course_data in courses.items():
            mark = self.marks.get(course_id)
            if mark is not None:
                credits.append(course_data.credits)
                marks.append(mark)
        avg_gpa = calculate_average_gpa(np.array(credits), np.array(marks))
        return avg_gpa

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, id, name, dob):
        self.students[id] = Student(id, name, dob)

    def add_course(self, id, name, credits):
        self.courses[id] = Course(id, name, credits)

    def enter_student_marks(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            for course_id, course in self.courses.items():
                mark = float(input(f"Enter mark for student {student_id} in course {course_id}: "))
                student.enter_marks(course_id, mark)
        else:
            print("Invalid student ID.")

    def show_student_marks(self):
        student_id = input("Enter student ID to show marks: ")
        if student_id in self.students:
            student = self.students[student_id]
            student.show_marks(self.courses)
        else:
            print("Invalid student ID.")

    def calculate_student_gpa(self):
        student_id = input("Enter student ID to calculate GPA: ")
        if student_id in self.students:
            student = self.students[student_id]
            avg_gpa = student.calculate_gpa(self.courses)
            print(f"Average GPA for student {student_id}: {avg_gpa}")
        else:
            print("Invalid student ID.")

    def list_students(self):
        print("\nStudents:")
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.name}, DOB: {student.dob}")

    def list_courses(self):
        print("\nCourses:")
        for course_id, course in self.courses.items():
            print(f"ID: {course_id}, Name: {course.name}, Credits: {course.credits}")

    def display_menu(self):
        print("\nSchool Management System Menu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enter Student Marks")
        print("4. Show Student Marks")
        print("5. Calculate Student GPA")
        print("6. List Students")
        print("7. List Courses")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                id = input("Enter student ID: ")
                name = input("Enter student name: ")
                dob = input("Enter student date of birth: ")
                self.add_student(id, name, dob)
            elif choice == '2':
                id = input("Enter course ID: ")
                name = input("Enter course name: ")
                credits = int(input("Enter course credits: "))
                self.add_course(id, name, credits)
            elif choice == '3':
                self.enter_student_marks()
            elif choice == '4':
                self.show_student_marks()
            elif choice == '5':
                self.calculate_student_gpa()
            elif choice == '6':
               self.list_students()
            elif choice == '7':
                self.list_courses()
            elif choice == '8':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the SchoolManagementSystem class and run the program
sms = SchoolManagementSystem()
sms.run()