import curses
import input as in_mod
import output as out_mod
from domains.student import Student
from domains.course import Course
import math
import numpy as np


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
        return self.__marks.get(course_id, {})


def main(stdscr):
    curses.curs_set(1)
    system = StudentMarkManagement()

    while True:
        out_mod.draw_menu(stdscr)
        key = stdscr.getch()

        if key == ord('1'):
            in_mod.input_students(stdscr, system)
        elif key == ord('2'):
            in_mod.input_courses(stdscr, system)
        elif key == ord('3'):
            in_mod.input_marks(stdscr, system)
        elif key == ord('4'):
            out_mod.sort_students_by_gpa(stdscr, system)
        elif key == ord('5'):
            out_mod.list_courses(stdscr, system)
        elif key == ord('6'):
            out_mod.show_student_marks(stdscr, system, in_mod.prompt_input)
        elif key == ord('0'):
            break


if __name__ == "__main__":
    curses.wrapper(main)