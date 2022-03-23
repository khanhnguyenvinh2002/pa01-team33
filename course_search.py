'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
OREN IS DOING HIS VIDEO
'''
from schedule import Schedule


SCHEDULE = Schedule()
SCHEDULE.load_courses()
SCHEDULE = SCHEDULE.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in SCHEDULE.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global SCHEDULE
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        if command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            SCHEDULE.load_courses()
            SCHEDULE = SCHEDULE.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            SCHEDULE = SCHEDULE.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            SCHEDULE = SCHEDULE.subject([subject])
        elif command in ['c', 'courses']:
            course = input("enter a coursenum:")
            SCHEDULE = SCHEDULE.course_num([course])
        elif command in ['i', 'instructor']:
            instructor = input('enter instructor\'s lastname to see courses they teach')
            SCHEDULE = SCHEDULE.lastname([instructor])
        elif command in ['ti', 'title']:
            title = input('enter a title')
            SCHEDULE = SCHEDULE.title([title])
        elif command in ['d', 'description']:
            description = input('enter a description')
            SCHEDULE = SCHEDULE.description([description])
        elif command in ['n', 'name']:
            course_name = input("enter a course name:")
            SCHEDULE = SCHEDULE.name([course_name])
        elif command in ['e', 'enrolled']:
            course_enrolled = input("enter a number of students:")
            SCHEDULE = SCHEDULE.enrolled([course_enrolled])
        elif command in ['l', 'limit']:
            course_limit = input("enter a number of students:")
            SCHEDULE = SCHEDULE.limit([course_limit])
        else:
            print('command',command,'is not supported')
            continue
        print("courses has",len(SCHEDULE.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in SCHEDULE.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''print_course prints a brief description of the course '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

def print_course_subject(course):
    print(course['subject'])



if __name__ == '__main__':
    topmenu()
