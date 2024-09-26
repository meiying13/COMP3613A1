from App.models import Student
from App.database import db

def create_student(student_id, firstname, lastname):
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        print(f'The student ID [ {student_id} ] is already exists !')
        return
    new_student = Student(
        student_id=student_id, 
        firstname=firstname, 
        lastname=lastname
    )
    db.session.add(new_student)
    db.session.commit()
    print(f'{student_id} | {firstname} {lastname} added !')
    return
    
    
def get_all_students():
    return Student.query.all()


def search_student_by_name(name):
    all_students = get_all_students()
    students = []
    for student in all_students:
        if student.firstname == name or student.lastname == name:
            students.append(student)
    return students


def search_student_by_id(student_id):
    return Student.query.filter_by(student_id=student_id).first()


def get_student_reviews(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    return student.get_reviews()