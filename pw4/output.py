import curses
def list_students(stdscr, system): 
    stdscr.clear()    
    stdscr.addstr("\nList of Student:\n", curses.A_BOLD)
    students = system.get_students()
    if not students:
        stdscr.addsttr("No students available.\n")
    else:
        for student in students:
            stdscr.addstr(f"{student.list_str()}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def list_courses(stdscr, system):
    stdscr.clear()
    stdscr.addstr("\nList of Course:\n", curses.A_BOLD)
    courses = system.get_coourses()
    if not courses:
        stdscr.addstr("No courses availabel.\n")
    else:
        for course in courses:
            stdscr.addstr(f"{course.list_str()}\n")
    stdscr.addstr("\nPress any key to coutinue...")
    stdscr.refresh()
    stdscr.getch()

def show_student_marks(stdscr, system, prompt_input_func):
    stdscr.clear()
    courses = system.get_courses()
    if not courses:
        stdscr.addstr("No courses available.\n")
        stdscr.addstr("\nPress any key to continue...")
        stdscr.refresh()
        stdscr.getch()
        return

    selected_course_id = prompt_input_func(stdscr, "Enter course ID to view marks: ")
    if not selected_course_id:
        return

    selected_course = None
    for course in courses:
        if course.get_id() == selected_course_id:
            selected_course = course
            break

    if selected_course is None:
        stdscr.clear()
        stdscr.addstr("\nCourse not found.\n")
        stdscr.addstr("\nPress any key to continue...")
        stdscr.refresh()
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(f"\nMarks for Course: {selected_course.get_name()}\n", curses.A_BOLD)
    
    marks_dict = system.get_marks_for_course(str(selected_course_id))
    students = system.get_students()

    if not marks_dict:
        stdscr.addstr("No marks found for this course.\n")
    else:
        for student in students:
            sid = student.get_id()
            if sid in marks_dict:
                stdscr.addstr(f"Student ID: {sid}, Name: {student.get_name()}, Mark: {marks_dict[sid]}\n")

    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def sort_students_by_gpa(stdscr, system):
    stdscr.clear()
    system.sort_studetns_by_gpa()
    stdscr.addstr("\nStudents sorted by GPQ:\n", curses.A_BOLD)
    students = system.get_students()
    if not students:
        stdscr.addstr("No students available.\n")
    else:
        for student in students:
            stdscr.addstr(f"{student.list_str()}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def draw_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("STUDENT MARK MANAGEMENT SYSTEM\n",curses.A_BOLD)
    stdscr.addstr("1. Input Students\n")
    stdscr.addstr("2. Input Courses\n")
    stdscr.addstr("3. Input Marks for Course\n")
    stdscr.addstr("4. List Students (Sorted by GPA Descending)\n")
    stdscr.addstr("5. List Courses\n")
    stdscr.addstr("6. Show Marks for Course\n")
    stdscr.addstr("0. Exit\n")
    stdscr.addstr("\nEnter choice: ", curses.A_BOLD)
    stdscr.refresh()