
print("STUDENT MARK MANAGEMENT")

def Course():
    global listCourses
    number = input("Number of courses:")
    for i in range(int(number)):
        print("Add new course: ")
        in4 = {'idCourse': input("Enter ID course:"), 'nameCourse': input("Enter the name of course:")}
        listCourses.append(in4)

def findStudent(id):
    global listStudents
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            return [i, listStudents[i]]
    return False

def addStudent():
    global infor
    Number = input("Number of students: ")
    for i in range(int(Number)):
        print("Add new student: ")
        global listStudents
        infor = {'id': '', 'name': '','DoB': '', 'mark': '' }
        id = input("Enter student ID: ")
        while True:
            if findStudent(id):
                print("ID existed, pls try again:")
                id = input()
            else:
                break
        infor['id'] = id
        infor['name'] = input("Enter student name:")
        infor['DoB'] = input("Enter DoB of Student:")
        listStudents.append(infor)

def displayCourse(listCourses):
    print('List courses: ')
    for course in listCourses:
        print(f"{course['idCourse']}: {course['nameCourse']}")

def displaylistStudents(listStudents):
    print('List students: ')
    for student in listStudents:
        print(f"{student['id']} - {student['name']} - {student['DoB']}")

def inputMark():
    global student
    for course in listCourses:
        marks = {}
        print(f"List marks for course {course['nameCourse']}")
        for student in listStudents:
            student['mark'] = float(input(f"Enter mark for {student['id']}: "))
            marks[student['id']] = student['mark']
            course.update(marks)

def displaylistMarks(course):
    for course in listCourses:
        namecourse = input("List marks for course: ")
        listMarks = dict(list(course.items())[2:4])
        print(listMarks)

listCourses = []
listStudents = []
course = {}
addStudent()
Course()
inputMark()
displayCourse(listCourses)
displaylistStudents(listStudents)
displaylistMarks(course)
