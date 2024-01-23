class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def enter_marks(self, course_id, mark):
        self.marks[course_id] = mark

    def show_marks(self, courses):
        print(f"\nMarks for student {self.id}:")
        for course_id, course_data in courses.items():
            mark = self.marks.get(course_id)
            if mark is not None:
                print(f"Course {course_id}, Name: {course_data.name}: {mark}")
            else:
                print(f"Course {course_id}, Name: {course_data.name}: Marks not available")


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_students(self):
        number_of_students = int(input("Enter the number of students: "))
        for _ in range(number_of_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            self.students[id] = Student(id, name, dob)

    def input_courses(self):
        number_of_courses = int(input("Enter the number of courses: "))
        for _ in range(number_of_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses[id] = Course(id, name)

    def select_course_and_enter_marks(self):
        for student_id, student in self.students.items():
            for course_id, course in self.courses.items():
                mark = float(input(f"Enter mark for student {student_id} in course {course_id}: "))
                student.enter_marks(course_id, mark)

    def list_courses(self):
        print("\nCourses:")
        for course_id, course in self.courses.items():
            print(f"ID: {course_id}, Name: {course.name}")

    def list_students(self):
        print("\nStudents:")
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.name}, DOB: {student.dob}")

    def show_student_marks(self):
        student_id = input("Enter student ID to show marks: ")
        if student_id in self.students:
            student = self.students[student_id]
            student.show_marks(self.courses)
        else:
            print("Invalid student ID.")

    def run(self):
        self.input_students()
        self.input_courses()
        self.select_course_and_enter_marks()

        while True:
            print("\nOptions:")
            print("1. List Courses")
            print("2. List Students")
            print("3. Show Student Marks")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.list_courses()
            elif choice == '2':
                self.list_students()
            elif choice == '3':
                self.show_student_marks()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
