

import sys
import re


def getCourse(line):
    """ This function takes in a row from a .csv file and returns the course

    :param line: This is the row for which the course must be found
    :return l_name, c_name: returns the lecturer's name as well as the course name
    """
    l_name, c_name = line.rstrip().split("/")    ##EE1
    return l_name, c_name   #EE2

def getCoursesForLects(lectsfn):
    ''' 
    This function groups related courses to lecturers

    :param lectsfn: This is the file which contains lecturers and courses
    :return courses: returns a dictionary which contains a list of courses for each lecturer
    '''
    courses = {}  # dictionary: for each lect returns list of courses
    lf = open(lectsfn)
    for line in lf:
        lect, course = getCourse(line)
        if lect in courses: # is the lecturer in the dictionary
            courses[lect].append(course)  # add course to the list ##EE3
        else:
            courses[lect] = [course]  
    lf.close()
    return courses

def getExams(examfname):
    '''
    This function takes a file containing exam data and returns the exams in a list

    :param examfname: This is the file which contains the exam data
    :return exams: This is a dictionary containing the exams time and location
    '''
    exams = {}
    ef = open(examfname)
    for line in ef:
        data = line.rstrip().split(",")
        exams[data[0]]=(data[1],data[2])
    ef.close()
    return exams

def getTimeTable(courses,exams):
    '''
    This function takes in courses and exam data, and returns a timetable

    :param courses: This is a dictionary of lecturers and their courses
    :para exams: This is a dictionary of exams containing their time and location
    :return ttable: This is a list containing lectueres and their exam times for the courses
    '''
    ttable = []  # nested list -- for each lect a list of exams
    for lect in sorted(courses.keys()):
        l_exams   = [] # build list of lecturer's exams
        l_courses = courses[lect] # get their courses
        for c in l_courses:
            if c not in exams:
                the_exam=("TBD","TBD")
            else:
                the_exam = exams[c]
            l_exams.append((c,the_exam))
        ttable.append((lect,l_exams)) # now we know the exams add it list
    return ttable

def showTimeTable(ttable):
    """
    This function displays a timetable using print()

    :param ttable: this is a list of lecturers and their exam times for courses
    :return: returns nothing
    """
    for (lect, l_exams) in ttable:
        print(lect)
        for c,ex in l_exams:
            print("   ",c,ex[0],ex[1])
        

if __name__ == "__main__":
    examfn    = sys.argv[1]
    lectsfn     = sys.argv[2]
    courses    = getCoursesForLects(lectsfn)
    exams     = getExams(examfn)
    tt = getTimeTable(courses,exams)
    showTimeTable(tt)
