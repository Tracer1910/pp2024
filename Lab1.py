def enter_student_data():
    students = {}
    number_of_students = int(input("Enter the number of students: "))
    for _ in range(number_of_students):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students[id] = {'name': name, 'dob': dob, 'marks': {}}
    return students

def enter_course_data():
    courses = {}
    number_of_courses = int(input("Enter the number of courses: "))
    for _ in range(number_of_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[id] = {'name': name}
    return courses

def select_course_and_enter_marks(students, courses):
    for student_id, student_data in students.items():
        for course_id, course_data in courses.items():
            mark = float(input(f"Enter mark for student {student_id} in course {course_id}: "))
            student_data['marks'][course_id] = mark

def list_courses(courses):
    print("\nCourses:")
    for course_id, course_data in courses.items():
        print(f"ID: {course_id}, Name: {course_data['name']}")

def list_students(students):
    print("\nStudents:")
    for student_id, student_data in students.items():
        print(f"ID: {student_id}, Name: {student_data['name']}, DOB: {student_data['dob']}")

def show_student_marks(students, courses):
    student_id = input("Enter student ID to show marks: ")
    if student_id in students:
        print(f"\nMarks for student {student_id}:")
        student_data = students[student_id]
        for course_id, course_data in courses.items():
            mark = student_data['marks'].get(course_id)
            if mark is not None:
                print(f"Course {course_id}, Name: {course_data['name']}: {mark}")
            else:
                print(f"Course {course_id}, Name: {course_data['name']}: Marks not available")
    else:
        print("Invalid student ID.")

students = enter_student_data()
courses = enter_course_data()

while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Show Student Marks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        list_courses(courses)
    elif choice == '2':
        list_students(students)
    elif choice == '3':
        show_student_marks(students, courses)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")