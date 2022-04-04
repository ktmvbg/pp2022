import input 
import output
import math
import json

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
    
    def to_json(self):
        return json.dumps(self._list, default=lambda x: x.__dict__)
    
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
    
    def load(self, file):
        json_data = json.load(file)
        for s in json_data:
            student = Student(s["_id"], s["_name"], s["_dob"])
            self.add(student)
        
        print("Loaded {} students!".format(len(self._list)))

    def input(self, number_of_students):
        for i in range(0, number_of_students):
            while(1):
                student = input.get_student_information()
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

    def load(self, file):
        json_data = json.load(file)
        for s in json_data:
            course = Course(s["_id"], s["_name"])
            self.add(course)
        print("Loaded {} courses!".format(len(self._list)))

    def input(self, number_of_courses):
        for i in range(0, number_of_courses):
            while(1):
                course = input.get_course_information()
                success, msg = self.add(course)
                if(success):
                    print("Added: {}".format(msg))
                    break
                else:
                    print(msg)
    
    def to_json(self):
        return json.dumps(self._list, default=lambda x: x.__dict__)

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
    
    def to_json(self):
        return json.dumps(self._list, default=lambda x: x.__dict__)
    
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
    
    def load(self, file, students, courses):
        self._students = students
        self._courses = courses
        json_data = json.load(file)
        for s in json_data:
            mark = Mark(s["_student_id"], s["_course_id"], s["_mark"])
            self.add(mark)
        print("Loaded {} marks!".format(len(self._list)))
    
    def list_by_course_id(self, course_id):
        m = [x for x in self._list if x._course_id == course_id]
        print("Number of marks course_id = {0}: {1}".format(course_id, len(m)))
        for mark in m:
            print(mark)
    
    def average_gpa_by_student(self, student_id):
        m = [x for x in self._list if x._student_id == student_id]
        if(len(m) == 0):
            return 0
        total_mark = 0
        for mark in m:
            total_mark += mark._mark
        return total_mark / len(m)

    def input(self, number_of_marks):
        for i in range(number_of_marks):
            while(1):
                mark = input.get_mark()
                success, msg = self.add(mark)
                if(success):
                    print("Added: {}".format(msg))
                    break
                else:
                    print(msg)  