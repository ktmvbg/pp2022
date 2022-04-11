import domains
import math
import json
import os
import zipfile
import pickle

def load_data():
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as data:
            students = domains.Students()
            courses = domains.Courses()
            marks = domains.Marks(students, courses)
            with data.open("students.pkl", mode = "r") as d:
                students.load(d)
            with data.open("courses.pkl", mode = "r") as d:
                courses.load(d)
            with data.open("marks.pkl", mode = "r") as d:
                marks.load(d)
            return (students, courses, marks)
    else:
        return (None, None, None)


def get_number_of_students():
    number_of_students = int(input("Enter number of students: "))
    return number_of_students

def get_student_information():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DoB: ")
    return domains.Student(student_id, student_name, student_dob)

def get_students(number_of_students, students = None):
    if students is None:
        students = domains.Students()
    students.input(number_of_students)
    with open("students.pkl", "wb") as f:
        pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
    return students

def get_number_of_courses():
    number_of_courses = int(input("Enter number of courses: "))
    return number_of_courses

def get_course_information():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    return domains.Course(course_id, course_name)

def get_courses(number_of_courses, courses = None):
    if courses is None:
        courses = domains.Courses()
    courses.input(number_of_courses)
    with open("courses.pkl", "wb") as f:
        pickle.dump(courses, f, pickle.HIGHEST_PROTOCOL)
    
    return courses

def get_number_of_marks():
    number_of_marks = int(input("Enter number of marks: "))
    return number_of_marks

def get_mark():
    student_id = input("Enter student id: ")
    course_id = input("Enter course id: ")
    mark = float(input("Enter mark: "))
    return domains.Mark(student_id, course_id, mark)

def get_marks(number_of_marks, students, courses, marks = None):
    if marks is None:
        marks = domains.Marks(students, courses)
    marks.input(number_of_marks)
    with open("marks.pkl", "wb") as f:
        pickle.dump(marks, f, pickle.HIGHEST_PROTOCOL)
    return marks

