from output import *
from input import *
from domains import *
import zipfile

def main():
    students, courses, marks = load_data()
    number_of_students = get_number_of_students()
    students = get_students(number_of_students, students)
    list_students(students)
    number_of_courses = get_number_of_courses()
    courses = get_courses(number_of_courses, courses)
    list_courses(courses)
    number_of_marks = get_number_of_marks()
    marks = get_marks(number_of_marks, students, courses, marks)
    list_mark(marks)
    list_mark_by_id("1", marks)
    print(marks.average_gpa_by_student("1"))
    s_s = sort_student_by_gpa_decending(students, marks)
    list_students(s_s)

    with zipfile.ZipFile("students.dat", "w") as compress_file:
        compress_file.write("students.txt", "students.txt")
        compress_file.write("courses.txt", "courses.txt")
        compress_file.write("marks.txt", "marks.txt")
 

if __name__ == "__main__":
    main()