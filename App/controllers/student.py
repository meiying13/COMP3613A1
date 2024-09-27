from App.models import Student
from App.database import db
from tabulate import tabulate

def create_student(student_id, firstname, lastname):
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        print(f'The student ID [ {student_id} ] already exists !')
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


def search_student_by_name(firstname, lastname):
    student = Student.query.filter_by(firstname=firstname, lastname=lastname).first()
    if not student:
        print(f'Student [ {firstname} {lastname} ] not found!')
        return
    return student


def search_student_by_id(student_id):
    student = Student.query.get(student_id)
    if not student:
        print(f'Student with ID [ {student_id} ] not found!')
        return
    return student


def print_students(students):
    headers = ["ID", "Name"]
    student_data = []
    for student in students:
        student_data.append([student.student_id, student.get_fullname()])
    print()
    print(tabulate(tabular_data=student_data, headers=headers, tablefmt="fancy_grid"))
    print()


def print_student(student: Student):    
    print()
    print(f'STUDENT ID\t-\t{student.student_id}')
    print(f'NAME\t\t-\t{student.get_fullname()}')
    print(f'OVERALL RATING\t-\t{student.get_overall_rating():.1f} star(s) ({len(student.reviews)} reviews)')
    print()
    
    
def print_student_reviews(student: Student):
    headers = ["Rating", "Author", "Review Comment"]
    reviews = []
    for review in student.reviews:
        author = review.author.get_fullname()
        reviews.append([review.rating, author, review.comment])
    
    print()
    print(f'STUDENT ID\t-\t{student.student_id}')
    print(f'NAME\t\t-\t{student.get_fullname()}')
    print(f'OVERALL RATING\t-\t{student.get_overall_rating():.1f} star(s) ({len(student.reviews)} reviews)')
    print(f'REVIEWS\t\t-')
    print(tabulate(tabular_data=reviews, headers=headers, tablefmt="fancy_grid"))
    print()
