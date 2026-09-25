print("STUDENT:")
n = int(input("Enter the number of students: "))
students = []

for i in range(n):
    print("Student information")
    student_id = input("Enter the student ID:")
    name = input("Enter the student NAME:")
    DoB = input("Enter the date of birth:")
    students.append((student_id, name, DoB))

for student in students:
    print("ID:", {student[0]}, "Name:", {student[1]}, "DoB:", {student[2]})


print("COURSE:")
n = int(input("Enter the number of courses: "))
courses = []

for i in range(n):
    print("Course information: ")
    course_id = input("Enter the course ID:")
    name = input("Enter the course NAME: ")
    courses.append((course_id, name))

for course in courses:
    print("course_ID:", {course[0]}, "Name:", {course[1]})


target_course_id = input("Enter the course ID:")

selected_course = None
for course in courses:
    if course[0] == target_course_id:
        selected_course = course
        break

if selected_course:
    print("STUDENT MARKS:")
    print("Course:", selected_course[1])

    course_marks = []
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} (ID: {student[0]}): "))
        course_marks.append((student[0], student[1], mark))

    for item in course_marks:
        print("ID:", item[0], "Name:", item[1], "Mark:", item[2])
else:
    print("Course ID not found!")