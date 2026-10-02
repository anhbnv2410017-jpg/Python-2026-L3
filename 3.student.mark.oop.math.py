import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def list_str(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob} | GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def list_str(self):
        return f"Course ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}"


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def add_student(self, student_id, name, dob):
        self.__students.append(Student(student_id, name, dob))

    def add_course(self, course_id, name, credits):
        self.__courses.append(Course(course_id, name, credits))

    def add_mark(self, course_id, student_id, mark):
        rounded_mark = math.floor(mark * 10) / 10
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = rounded_mark

    def calculate_gpa(self):
        for student in self.__students:
            sid = student.get_id()
            student_marks = []
            credits_list = []

            for course in self.__courses:
                cid = course.get_id()
                if cid in self.__marks and sid in self.__marks[cid]:
                    student_marks.append(self.__marks[cid][sid])
                    credits_list.append(course.get_credits())

            if student_marks and credits_list:
                marks_arr = np.array(student_marks)
                credits_arr = np.array(credits_list)
                gpa = np.average(marks_arr, weights=credits_arr)
                student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)

    def sort_students_by_gpa(self):
        self.calculate_gpa()
        if not self.__students:
            return
        gpas = np.array([s.get_gpa() for s in self.__students])
        sorted_indices = np.argsort(gpas)[::-1]
        self.__students = [self.__students[i] for i in sorted_indices]

    def get_marks_for_course(self, course_id):
        if course_id in self.__marks:
            return self.__marks[course_id]
        return {}


def prompt_input(stdscr, prompt_text):
    stdscr.clear()
    stdscr.addstr(1, 2, prompt_text, curses.A_BOLD)
    stdscr.addstr(3, 2, "> ")
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 4).decode('utf-8')
    curses.noecho()
    return val


def draw_screen(stdscr, system):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== STUDENT MARK MANAGEMENT SYSTEM (CURSES UI) ===", curses.A_BOLD | curses.A_UNDERLINE)
    stdscr.addstr(3, 2, "1. Input Students")
    stdscr.addstr(4, 2, "2. Input Courses")
    stdscr.addstr(5, 2, "3. Input Marks for Course")
    stdscr.addstr(6, 2, "4. List Students (Sorted by GPA Descending)")
    stdscr.addstr(7, 2, "5. List Courses")
    stdscr.addstr(8, 2, "6. Show Marks for Course")
    stdscr.addstr(9, 2, "0. Exit")
    stdscr.addstr(11, 2, "Enter your choice: ", curses.A_BOLD)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(1)
    system = StudentMarkManagement()

    while True:
        draw_screen(stdscr, system)
        key = stdscr.getch()

        if key == ord('1'):
            n_str = prompt_input(stdscr, "Enter the number of students:")
            if n_str.isdigit():
                for i in range(int(n_str)):
                    sid = prompt_input(stdscr, f"Student {i+1} ID:")
                    name = prompt_input(stdscr, f"Student {i+1} Name:")
                    dob = prompt_input(stdscr, f"Student {i+1} DoB:")
                    system.add_student(sid, name, dob)

        elif key == ord('2'):
            n_str = prompt_input(stdscr, "Enter the number of courses:")
            if n_str.isdigit():
                for i in range(int(n_str)):
                    cid = prompt_input(stdscr, f"Course {i+1} ID:")
                    cname = prompt_input(stdscr, f"Course {i+1} Name:")
                    credits_str = prompt_input(stdscr, f"Course {i+1} Credits:")
                    credits = int(credits_str) if credits_str.isdigit() else 0
                    system.add_course(cid, cname, credits)

        elif key == ord('3'):
            cid = prompt_input(stdscr, "Enter Course ID to input marks:")
            courses = system.get_courses()
            course_exists = any(c.get_id() == cid for c in courses)
            
            if course_exists:
                students = system.get_students()
                for s in students:
                    mark_str = prompt_input(stdscr, f"Enter mark for {s.get_name()} (ID: {s.get_id()}):")
                    try:
                        mark = float(mark_str)
                        system.add_mark(cid, s.get_id(), mark)
                    except ValueError:
                        pass

        elif key == ord('4'):
            stdscr.clear()
            system.sort_students_by_gpa()
            stdscr.addstr(1, 2, "=== STUDENT LIST SORTED BY GPA DESCENDING ===", curses.A_BOLD)
            students = system.get_students()
            row = 3
            if not students:
                stdscr.addstr(row, 2, "No students available.")
            else:
                for s in students:
                    stdscr.addstr(row, 2, s.list_str())
                    row += 1
            stdscr.addstr(row + 1, 2, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()

        elif key == ord('5'):
            stdscr.clear()
            stdscr.addstr(1, 2, "=== COURSE LIST ===", curses.A_BOLD)
            courses = system.get_courses()
            row = 3
            if not courses:
                stdscr.addstr(row, 2, "No courses available.")
            else:
                for c in courses:
                    stdscr.addstr(row, 2, c.list_str())
                    row += 1
            stdscr.addstr(row + 1, 2, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()

        elif key == ord('6'):
            cid = prompt_input(stdscr, "Enter Course ID to view marks:")
            stdscr.clear()
            stdscr.addstr(1, 2, f"=== MARKS FOR COURSE: {cid} ===", curses.A_BOLD)
            marks_dict = system.get_marks_for_course(cid)
            students = system.get_students()
            row = 3
            if not marks_dict:
                stdscr.addstr(row, 2, "No marks found for this course.")
            else:
                for s in students:
                    sid = s.get_id()
                    if sid in marks_dict:
                        stdscr.addstr(row, 2, f"ID: {sid} | Name: {s.get_name()} | Mark: {marks_dict[sid]}")
                        row += 1
            stdscr.addstr(row + 1, 2, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()

        elif key == ord('0'):
            break


if __name__ == "__main__":
    curses.wrapper(main)
