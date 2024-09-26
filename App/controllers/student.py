from App.models import Student
from App.database import db

def create_student(student_id, firstname, lastname):
    new_student = Student(
        student_id=student_id, 
        firstname=firstname, 
        lastname=lastname
    )
    db.session.add(new_student)
    db.session.commit()
    
    
def get_all_students():
    return Student.query.all()