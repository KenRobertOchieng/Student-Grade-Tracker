# Student Grade Tracker

A simple Python-based application using SQLAlchemy to manage students, courses, enrollments, and grades.

## Features

* **Students**: Store basic student information.
* **Courses**: Define course codes, titles, and semesters.
* **Enrollments**: Track which students are enrolled in which courses, with enrollment dates.
* **Assignments & Grades**: Record assignment details and link student scores and feedback.

## Requirements

* Python 3.7+
* SQLAlchemy
* SQLite (for local development)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/student-grade-tracker.git
   cd student-grade-tracker
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install sqlalchemy
   ```

## Database Setup

Tables are created automatically in `official_database.db` when you run:

```python
from models import Base, engine
Base.metadata.create_all(engine)
```

## Usage

1. Import models and session:

   ```python
   from models import Student, Course, Enrollment, Assignment, Grade, session
   ```
2. Create and commit objects:

   ```python
   student = Student(first_name='Jane', last_name='Doe', email='jane@example.com')
   course = Course(code='MATH101', title='Mathematics', semester=1)
   enrollment = Enrollment(student=student, course=course)
   session.add_all([student, course, enrollment])
   session.commit()
   ```
3. Query data:

   ```python
   # List all courses for a student + date enrolled
   s = session.query(Student).first()
   for e in s.enrollments:
       print(e.course.title, e.enrollment_date)

    # across all students—show everyone’s average:
    averages = (session.query(Student.first_name,func.avg(Grade.score).label("avg_score")).join(Grade).group_by(Student.id).all())

    for name, avg in averages:
      print(f"{name}: {avg:.1f}") 

    # filter all students
      all_the_students=session.query(Student).all()
          print(all_the_students)     
   ```

## Project Structure

```
student-grade-tracker/
├── models.py           # SQLAlchemy models and engine setup
├── debugging.py             # For texting our codes if they are working
├── official_database.db# SQLite database file
├── README.md           # Project overview (this file)
└── requirements.txt    # for setting up a plan for our project
```

## Contributing

Feel free to open issues or submit pull requests to improve this tracker.

## License

This project is open source and available under the MIT License.
