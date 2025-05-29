from models import Student ,Course ,session ,Enrollment ,date ,Grade,Assignment
from sqlalchemy import func

# create student object
student_1=Student(first_name='ken',last_name='robert',email='kenrobertochi@gmail.com')
student_2=Student(first_name='collins',last_name='mayienga',email='collinsmayienga@gmail.com')
student_3=Student(first_name='alfred',last_name='kiprotich',email='alfredkiprotich@gmail.com')
student_4=Student(first_name='sarah',last_name='ouma',email='sarahouma@gmail.com')
student_5=Student(first_name='maina',last_name='lucky',email='mainalucky@gmail.com')
student_6=Student(first_name='joseph',last_name='semets',email='josephsemeta@gmail.com')
student_7=Student(first_name='pedro',last_name='yamal',email='pedroyamal@gmail.com')
student_8=Student(first_name='william',last_name='griffins',email='williamgriffins@gmail.com')
student_9=Student(first_name='brian',last_name='nyangaria',email='briannyangaria@gmail.com')
student_10=Student(first_name='zakayo',last_name='ibrahim',email='zakayoibrahim@gmail.com')

# create courses object
course_1=Course(code=104,title='mathematics',semester=2)
course_2=Course(code=104,title='geography',semester=10)
course_3=Course(code=104,title='physics',semester=8)
course_4=Course(code=104,title='chemistry',semester=1)
course_5=Course(code=104,title='english',semester=5)
course_6=Course(code=104,title='business',semester=3)
course_7=Course(code=104,title='history',semester=9)
course_8=Course(code=104,title='computer science',semester=4)
course_9=Course(code=104,title='kiswahili',semester=6)
course_10=Course(code=104,title='IT',semester=7)

#links
enrollments=[
Enrollment(student=student_1, course=course_7,enrollment_date=date(2016,3,14)),
Enrollment(student=student_2,course=course_6,enrollment_date=date(2018,9,7)),
Enrollment(student=student_3,course=course_1,enrollment_date=date(2020,5,27)),
Enrollment(student=student_4,course=course_4,enrollment_date=date(2013,6,1)),
Enrollment(student=student_5,course=course_5,enrollment_date=date(2021,1,20)),
Enrollment(student=student_6,course=course_3,enrollment_date=date(2022,4,19)),
Enrollment(student=student_7,course=course_5,enrollment_date=date(2015,12,25)),
Enrollment(student=student_8,course=course_10,enrollment_date=date(2024,9,15)),
Enrollment(student=student_9,course=course_2,enrollment_date=date(2024,9,11)),
Enrollment(student=student_10,course=course_4,enrollment_date=date(2025,2,6))
]

# assignment to grade
term_three_exam = Assignment(title="term three exam",max_score=20, course=course_10)

grades=[
Grade(student=student_5,assignment=term_three_exam,score=89),
Grade(student=student_2,assignment=term_three_exam,score=66),
Grade(student=student_3,assignment=term_three_exam,score=79),
Grade(student=student_2,assignment=term_three_exam,score=99),
Grade(student=student_5,assignment=term_three_exam,score=65),
Grade(student=student_3,assignment=term_three_exam,score=76),
Grade(student=student_2,assignment=term_three_exam,score=40),
Grade(student=student_10,assignment=term_three_exam,score=54),
Grade(student=student_9,assignment=term_three_exam,score=100),
Grade(student=student_10,assignment=term_three_exam,score=84)
]

# add to session
session.add_all([student_1,student_2,student_3,student_4,student_5,
                 student_6,student_7,student_8,student_9,student_10,
                 course_1,course_2,course_3,course_4,course_5,course_6,
                 course_7,course_8,course_9,course_10,
                 *enrollments,term_three_exam,
                 term_three_exam,*grades
])

# commit changes
session.commit()

# filter all students
all_the_students=session.query(Student).all()
print(all_the_students)

# filter a single student by mail
my_filter=session.query(Student).filter_by(email='mainalucky@gmail.com').first()

# list all enrollments for a student (and the course + date)
if my_filter:
    print(my_filter.first_name, my_filter.last_name)
    for e in my_filter.enrollments:
        print(f"{e.course.title} – enrolled on {e.enrollment_date}")
else:
    print("No student found with that email.")

# across all students—show everyone’s average:
averages = (session.query(Student.first_name,func.avg(Grade.score).label("avg_score")).join(Grade).group_by(Student.id).all())

for name, avg in averages:
    print(f"{name}: {avg:.1f}")    













