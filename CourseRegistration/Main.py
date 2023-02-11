#from FileName import Class
from Student import Student
from Course import Course
from Teacher import Teacher
import random  #built in module, no need for the from syntax

masterStudentList = []
masterCourseList = []
masterTeacherList = []

def loadStudent():
    #read from the DB
    file1 = open("StudentDatabase.csv","r")
    file = file1.readlines()
    for line in file:
        first,last = line.rstrip().split(",")
        #create new student object
        newStudent = Student(first,last)
        #add student to masterStudentList
        masterStudentList.append(newStudent)

def loadTeacher():
     #read from the DB
     file1 = open("TeacherDatabase.csv","r")
     file = file1.readlines()
     for line in file:
          id,first,last = line.rstrip().split(",")
          #create new student object
          newTeacher = Teacher(first,last,id)
          #add student to masterStudentList
          masterTeacherList.append(newTeacher)

def printStudents():
    #print out each student and their courses
    for student in masterStudentList:
        print(student)
        
def printTeachers():
    #print out each student and their courses
    for teacher in masterTeacherList:
        print(teacher)

def loadCourse():
    #read in the csv file or pull from db
    file1 = open("CourseCatalog.csv","r")
    file = file1.readlines()
    for line in file:
        id,name,description = line.rstrip().split(",")
        #create course object
        newCourse = Course(id,name)
        #save course object to masterCourseList
        masterCourseList.append(newCourse)
     
def assignCourses():
    #randomly assigning courses to students
    for student in masterStudentList:
        listOfCourses=masterCourseList.copy()
        #loop 4 times because we have 4 class to add
        for i in range(4):       #never use the i
            courseToAdd = listOfCourses.pop(random.randrange(0,len(listOfCourses)))
            student.addCourse(courseToAdd)
            #watch out to not duplicate a course in the schedule
            
def assignTeacherCourses():
    #randomly assigning courses to students
    for teacher in masterTeacherList:
        listOfCourses=masterCourseList.copy()
        #loop 4 times because we have 4 class to add
        for i in range(3):       #never use the i
            courseToAdd = listOfCourses.pop(random.randrange(0,len(listOfCourses)))
            teacher.addCourse(courseToAdd)
            #watch out to not duplicate a course in the schedule

def printOutSchedules():
    for student in masterStudentList:
        fileToWriteTo = open(f"{student.lastName}_{student.firstName}.txt","w")
        fileToWriteTo.write(student.__str__())  #print does the __str__ for you -> write does not
        fileToWriteTo.close()
        
def printOutTeacherSchedules():
    for teacher in masterTeacherList:
        fileToWriteTo = open(f"{teacher.id}_{teacher.lastName}_{teacher.firstName}.txt","w")
        fileToWriteTo.write(teacher.__str__())  #print does the __str__ for you -> write does not
        fileToWriteTo.close()

loadStudent()
loadCourse()
assignCourses()
printStudents()
printOutSchedules()

loadTeacher()
loadCourse()
assignTeacherCourses()
printTeachers()
printOutTeacherSchedules()