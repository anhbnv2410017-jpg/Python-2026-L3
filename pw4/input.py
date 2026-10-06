import curses


def prompt_input(stdscr, prompt_text):
    stdscr.clear()
    stdscr.addstr(1, 2, prompt_text, curses.A_BOLD)
    stdscr.addstr(3, 2, "> ")
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 4).decode('utf-8').strip()
    curses.noecho()
    return val


def input_students(stdscr, system):
    n_str = prompt_input(stdscr, "Enter the number of students:")
    if n_str.isdigit():
        for i in range(int(n_str)):
            sid = prompt_input(stdscr, f"Student {i+1} ID:")
            name = prompt_input(stdscr, f"Student {i+1} Name:")
            dob = prompt_input(stdscr, f"Student {i+1} DoB:")
            
            system.add_student(sid, name, dob)


def input_courses(stdscr, system):
    n_str = prompt_input(stdscr, "Enter the number of courses:")
    if n_str.isdigit():
        for i in range(int(n_str)):
            cid = prompt_input(stdscr, f"Course {i+1} ID:")
            cname = prompt_input(stdscr, f"Course {i+1} Name:")
            credits_str = prompt_input(stdscr, f"Course {i+1} Credits:")
            credits = int(credits_str) if credits_str.isdigit() else 0
            
            system.add_course(cid, cname, credits)


def input_marks(stdscr, system):
    cid = prompt_input(stdscr, "Enter Course ID to input marks:")
    if not cid:
        return

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
    else:
        stdscr.clear()
        stdscr.addstr(1, 2, "Course ID not found!\n")
        stdscr.addstr(3, 2, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()