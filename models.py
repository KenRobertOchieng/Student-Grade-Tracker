from sqlalchemy import create_engine , String , Column , Integer , ForeignKey , Text , Date, UniqueConstraint
from sqlalchemy.orm import sessionmaker , declarative_base ,relationship
from datetime import date

# initialize database engine
engine=create_engine('sqlite:///official.db')

# configure our session
Session=sessionmaker(bind=engine)
session=Session()

# initialize our class maker
Base=declarative_base()

# defining association table(Students--->Courses)
class Enrollment(Base):

    __tablename__='enrollments'

    student_id = Column(
        Integer,
        ForeignKey('student.id'),
        primary_key=True,
        autoincrement=False
        )
    
    course_id=Column(
        Integer,
        ForeignKey('course.id'),
        primary_key=True,
        autoincrement=False
        )
    
    enrollment_date=Column(Date, default=date.today)

    student=relationship('Student',back_populates='enrollments')
    course=relationship('Course',back_populates='enrollments')

# defining our table name(Student)
class Student(Base):

    __tablename__='student'

    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String(25),unique=True)
    enrollments=relationship('Enrollment',back_populates='student')
    grades=relationship('Grade',back_populates='student')

     # what to be seen when we print our object
    def __repr__(self) :
        return f"<Student({self.first_name} {self.last_name} ,{self.id})>"

# defining table name(Course) 
class Course(Base):
    __tablename__='course'

    id=Column(Integer, primary_key=True)
    code=Column(String)
    title=Column(String)
    semester=Column(Integer)
    enrollments=relationship('Enrollment',back_populates='course')
    assignments = relationship('Assignment',back_populates='course')

# defining table name(Assignments)
class Assignment(Base):
    __tablename__='assignment'

    id=Column(Integer, primary_key=True)
    title=Column(String)
    max_score=Column(Integer)
    course_id=Column(
        Integer, 
        ForeignKey('course.id'))
    
    course= relationship('Course',back_populates='assignments')
    grades=relationship('Grade',back_populates='assignment')

# defining association table(Students---> Assignments)
class Grade(Base):
    __tablename__='grade'
    student_id=Column(
        Integer,ForeignKey('student.id'),
        primary_key=True,
        autoincrement=False
        )
    
    assignment_id=Column(
        Integer,ForeignKey('assignment.id'),
        primary_key=True,
        autoincrement=False
        )
    
    score=Column(Integer)
    student=relationship('Student',back_populates='grades')
    assignment=relationship('Assignment',back_populates='grades')

#create tables
Base.metadata.create_all(engine)    



