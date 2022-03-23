import numpy
import math
def get_number_of_students():
    number_of_students = int(input("Enter number of students: "))
    return number_of_students

def get_student_information():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DoB: ")
    return Student(student_id, student_name, student_dob)

def get_students(number_of_students):
    students = Students()
    students.input(number_of_students)
    return students

def list_students(students):
    students.list()

def get_number_of_courses():
    number_of_courses = int(input("Enter number of courses: "))
    return number_of_courses

def get_course_information():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    return Course(course_id, course_name)

def get_courses(number_of_courses):
    courses = Courses()
    courses.input(number_of_courses)
    return courses

def list_courses(courses):
    courses.list()

def get_number_of_marks():
    number_of_marks = int(input("Enter number of marks: "))
    return number_of_marks

def get_mark():
    student_id = input("Enter student id: ")
    course_id = input("Enter course id: ")
    mark = float(input("Enter mark: "))
    return Mark(student_id, course_id, mark)

def get_marks(number_of_marks, students, courses):
    marks = Marks(students, courses)
    marks.input(number_of_marks)
    return marks

def list_mark(marks):
    marks.list()

def list_mark_by_id(course_id, marks):
    marks.list_by_course_id(course_id)

def get_avg_gpa(marks, student_id):
    return marks.average_gpa_by_student(student_id)

def sort_student_by_gpa_decending(students, marks):
    students.sort_by_gpa(marks)
    return students
def main():
    number_of_students = get_number_of_students()
    students = get_students(number_of_students)
    list_students(students)
    number_of_courses = get_number_of_courses()
    courses = get_courses(number_of_courses)
    list_courses(courses)
    number_of_marks = get_number_of_marks()
    marks = get_marks(number_of_marks, students, courses)
    list_mark(marks)
    list_mark_by_id("1", marks)
    print(marks.average_gpa_by_student("1"))
    s_s = sort_student_by_gpa_decending(students, marks)
    list_students(s_s)


class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
    def set_id(self, id):
        self._id = id
    def get_id(self):
        return self._id
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_dob(self, dob):
        self._dob = dob
    def get_dob(self):
        return self._dob
    
    def __repr__(self):
        return "Student<id={0},name={1},DoB={2}>".format(self._id, self._name, self._dob)

class Students:
    def __init__(self):
        self._list = []
    
    def add(self, student):
        dup = len([x for x in self._list if x._id == student._id]) > 0
        if(dup):
            return (False, "Dup student")
        self._list.append(student)
        return (True, student)
    
    def list(self):
        print("Number of students: {0}".format(len(self._list)))
        for student in self._list:
            print(student)
    def input(self, number_of_students):
        for i in range(0, number_of_students):
            while(1):
                student = get_student_information()
                success, msg = self.add(student)
                if(success):
                    print("Added: {}".format(msg))
                    break
                else:
                    print(msg)
    def sort_by_gpa(self, marks)                :
        self._list.sort(key = lambda x: marks.average_gpa_by_student(x._id), reverse=True)
class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def set_id(self, id):
        self._id = id
    def get_id(self):
        return self._id
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def __repr__(self):
        return "Course<id={0},name={1}>".format(self._id, self._name)

class Courses:
    def __init__(self):
        self._list = []
    
    def add(self, course):
        dup = len([x for x in self._list if x._id == course._id]) > 0
        if(dup):
            return (False, "Dup course id")
        self._list.append(course)
        return (True, course)
    
    def list(self):
        print("Number of courses: {0}".format(len(self._list)))
        for course in self._list:
            print(course)
    def input(self, number_of_courses):
        for i in range(0, number_of_courses):
            while(1):
                course = get_course_information()
                success, msg = self.add(course)
                if(success):
                    print("Added: {}".format(msg))
                    break
                else:
                    print(msg)      

class Mark:
    def __init__(self, student_id, course_id, mark):
        self._student_id = student_id
        self._course_id = course_id
        self._mark = math.floor(mark*10)/10
    def set_student_id(self, student_id):
        self._student_id = student_id
    def get_student_id(self):
        return self._student_id
    def set_course_id(self, course_id):
        self._course_id = course_id
    def get_course_id(self):
        return self._course_id
    def set_mark(self, mark):
        self._mark = math.floor(mark*10)/10
    def get_mark(self):
        return self._mark
    def __repr__(self):
        return "Mark<student_id={0},course_id={1},mark={2}>".format(
            self._student_id, self._course_id, self._mark
        )

class Marks:
    def __init__(self, students, courses):
        self._list = []
        self._students = students
        self._courses = courses
    
    def add(self, mark):
        s = len([x for x in self._students._list if x._id == mark._student_id])
        if(s == 0):
            return (False, "Invalid student id")
        c = len([x for x in self._courses._list if x._id == mark._course_id])
        if(c == 0):
            return (False, "Invalid course id")
        m = len([x for x in self._list if x._course_id == mark._course_id
            and x._student_id == mark._student_id])
        if(m > 0):
            return (False, "Duplicate")
        self._list.append(mark)
        return (True, mark)
    
    def list(self):
        print("Number of marks: {0}".format(len(self._list)))
        for mark in self._list:
            print(mark)
    
    def list_by_course_id(self, course_id):
        m = [x for x in self._list if x._course_id == course_id]
        print("Number of marks course_id = {0}: {1}".format(course_id, len(m)))
        for mark in m:
            print(mark)
    
    def average_gpa_by_student(self, student_id):
        m = [x for x in self._list if x._student_id == student_id]
        if(len(m) == 0):
            return (False, "Invalid student id")
        total_mark = 0
        for mark in m:
            total_mark += mark._mark
        return total_mark / len(m)

    def input(self, number_of_marks):
        for i in range(number_of_marks):
            while(1):
                mark = get_mark()
                success, msg = self.add(mark)
                if(success):
                    print("Added: {}".format(msg))
                    break
                else:
                    print(msg)     

if __name__ == "__main__":
    main()