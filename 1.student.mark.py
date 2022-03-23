def get_number_of_students():
    number_of_students = int(input("Enter number of students: "))
    return number_of_students

def get_student_information():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DoB: ")
    return (student_id, student_name, student_dob)

def get_students(number_of_students):
    students = []
    for i in range(0, number_of_students):
        while(1):
            student = get_student_information()
            dup = len([x for x in students if x[0] == student[0]]) > 0
            if(dup):
                print("Invalid student id")
            else:
                students.append(student)
                print("Added: {}".format(student))
                break
    return students

def list_students(students):
    print("Number of students: {0}".format(len(students)))
    for student in students:
        print(student)

def get_number_of_courses():
    number_of_courses = int(input("Enter number of courses: "))
    return number_of_courses

def get_course_information():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

def get_courses(number_of_courses):
    courses = []
    for i in range(0, number_of_courses):
        while(1):
            course = get_course_information()
            dup = len([x for x in courses if x[0] == course[0]]) > 0
            if(dup):
                print("Invalid course id")
            else:
                courses.append(course)
                print("Added: {}".format(course))
                break
    return courses

def list_courses(courses):
    print("Number of courses: {0}".format(len(courses)))
    for course in courses:
        print(course)

def get_number_of_marks():
    number_of_marks = int(input("Enter number of marks: "))
    return number_of_marks

def get_mark():
    student_id = input("Enter student id: ")
    course_id = input("Enter course id: ")
    mark = float(input("Enter mark: "))
    return (student_id, course_id, mark)

def get_marks(number_of_marks, students, courses):
    marks = []
    for i in range(number_of_marks):
        while(1):
            mark = get_mark()
            s = len([x for x in students if x[0] == mark[0]])
            if(s == 0):
                print("Invalid student id")
                continue
            c = len([x for x in courses if x[0] == mark[1]])
            if(c == 0):
                print("Invalid course id")
                continue
            m = len([x for x in marks if x[0] == mark[0] and x[1] == mark[1]])
            if(m > 0):
                print("Duplicate")
                continue
            marks.append(mark)
            print("Added: {}".format(mark))
            break
    return marks

def list_mark(marks):
    print("Number of marks: {0}".format(len(marks)))
    for mark in marks:
        print(mark)

def list_mark_by_id(course_id, marks):
    m = [x for x in marks if x[1] == course_id]
    print("Number of marks course_id = {0}: {1}".format(course_id, len(m)))
    for mark in m:
        print(mark)

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


if __name__ == "__main__":
    main()