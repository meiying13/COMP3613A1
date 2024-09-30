from App.models import Student
from App.database import db
from tabulate import tabulate
from typing import Union


def create_student(student_id: int, firstname: str, lastname: str, programme: str) -> bool:
    student: Student | None = Student.query.filter_by(student_id=student_id).first()
    if student:
        print(f'The student ID [ {student_id} ] already exists!')
        return False
    new_student = Student(
        student_id=student_id, 
        firstname=firstname, 
        lastname=lastname,
        programme=programme
    )
    db.session.add(new_student)
    db.session.commit()
    return True

def get_all_students() -> list[Student]:
    return Student.query.all()

def search_student_by_name(firstname: str, lastname: str) -> list[Student]:
    students: list[Student] = Student.query.filter(
        Student.firstname.ilike(f"%{firstname}%") &
        Student.lastname.ilike(f"%{lastname}%")
    ).all()
    if not students:
        print(f'Student [ {firstname} {lastname} ] not found!')
        return None
    return students

def search_student_by_id(student_id: int) -> Student | None:
    student: Student | None = Student.query.get(student_id)
    if not student:
        print(f'Student with ID [ {student_id} ] not found!')
        return None
    return student

def print_students(students: list[Student]) -> None:
    headers: list[str] = ["ID", "Name", "Programme of Study"]
    student_data: list[list[str]] = []
    for student in students:
        student_data.append([student.student_id, student.get_fullname(), student.programme])
    print()
    print(tabulate(tabular_data=student_data, headers=headers, tablefmt="fancy_grid"))
    print()

def print_student(student: Student) -> None:
    print()
    print(f'STUDENT ID\t-\t{student.student_id}')
    print(f'NAME\t\t-\t{student.get_fullname()}')
    print(f'PROGRAMME\t-\t{student.programme}')
    print(f'OVERALL RATING\t-\t{student.get_overall_rating():.1f} star(s) ({len(student.reviews)} reviews)')
    print()

def print_student_reviews(student: Student) -> None:
    headers: list[str] = ["Rating", "Author", "Review Comment"]
    reviews: list[list[Union[int, str]]] = []
    for review in student.reviews:
        author: str = review.author.get_fullname()
        reviews.append([review.rating, author, review.comment])
    print()
    print(f'STUDENT ID\t-\t{student.student_id}')
    print(f'NAME\t\t-\t{student.get_fullname()}')
    print(f'PROGRAMME\t-\t{student.programme}')
    print(f'OVERALL RATING\t-\t{student.get_overall_rating():.1f} star(s) ({len(student.reviews)} reviews)')
    print(f'REVIEWS\t\t-')
    print(tabulate(tabular_data=reviews, headers=headers, tablefmt="fancy_grid"))
    print()
