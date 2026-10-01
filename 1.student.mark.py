def student_number():
    student_number = input("Enter your student number: ")
    return student_number
def student_info():
    student_info = input("Enter your student info: ")
    return student_info
def student_id():
    id = input("Enter your student ID: ")
    return id
def student_name():
    name = input("Enter your name: ")
    return name
def student_dob():
    dob = input("Enter your date of birth (dd-mm-yy): ")
    return dob
def course():
    course = input("Enter your course: ")
    return course
def course_id():
    course_id = input("Enter your course ID: ")
    return course_id
def course_name():
    course_name = input("Enter your course name: ")
    return course_name
def show_student_marks(marks, students):
    c_id = input("Enter course ID to show student marks: ")
    if c_id not in marks:
        print("No marks available for this course.")
        return
    print(f"\n--- Marks for course {c_id} ---")
    for student in students:
        s_id = student["id"]
        if s_id in marks[c_id]:
            print(f"Student ID: {s_id} | Name: {student['name']} | Mark: {marks[c_id][s_id]}")
        else:
            print(f"Student ID: {s_id} | Name: {student['name']} | Mark: Not available")
def input_marks(courses, students, marks):
    print(This function did not fully deployde yet.")
course_list = ["ICT", "CS", "IT", "SE", "DS"]
course_id_list = ["ICT101", "CS102", "IT103", "SE104", "DS105"]
course_name_list = ["Introduction to Computer Science", "Data Structures", "Web Development", "Software Engineering", "Data Science"]
student_list = ["A", "B", "C", "D", "E"]
students_info_list = ["A1", "B2", "C3", "D4", "E5"]
student_id_list = ["S001", "S002", "S003", "S004", "S005"]
student_dob_list = ["01-01-2000", "02-02-2001", "03-03-2002", "04-04-2003", "05-05-2004"]
marks = {}
courses = [] 
students = [] 
while True:
        print("\n======== STUDENT MARK MANAGEMENT ========")
        print("1. Input number of students and their info")
        print("2. Input number of courses and their info")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a given course")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")
        if choice == '1':
            num_students = student_number()
            students = student_info()
        if choice == '2':
            num_courses = course()
            pass
        if choice == '3':
            if not courses or not students:
                print("Courses or students are not exist/unavailable.")
            else:
                input_marks(courses, students, marks)
        if choice == '4':
            print("Students list:", students_info_list)
        if choice == '5':
            print("Courses list:", course_name_list)
        if choice == '6':
            show_student_marks(marks, students)
        if choice == '7':
            print("Exiting program...")
            break
