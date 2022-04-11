
def list_students(students):
    students.list()

def list_courses(courses):
    courses.list()

def list_mark(marks):
    marks.list()

def list_mark_by_id(course_id, marks):
    marks.list_by_course_id(course_id)

def get_avg_gpa(marks, student_id):
    return marks.average_gpa_by_student(student_id)

def sort_student_by_gpa_decending(students, marks):
    students.sort_by_gpa(marks)
    return students
