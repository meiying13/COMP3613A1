from App.models import Review, Staff, Student
from App.database import db
from tabulate import tabulate
from typing import Union


def create_review(student_id: int, username: str, rating: int, comment: str) -> bool:
    staff: Staff | None = Staff.query.filter_by(username=username).first()
    if staff is None:
        print(f'\nStaff with username [ {username} ] not found!\n')
        return False

    student: Student | None = Student.query.filter_by(student_id=student_id).first()
    if student is None:
        print(f'\nStudent with ID [ {student_id} ] not found!\n')
        return False

    if rating < 1 or rating > 5:
        print(f'\nInvalid rating [ {rating} ]. Rating must be between 1 (Very Poor) and 5 (Excellent).\n')
        return False

    new_review = Review(
        student_id=student.student_id, 
        staff_id=staff.id, 
        rating=rating, 
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    return True

    
def get_all_reviews() -> list[Review]:
    return Review.query.all()

def get_reviews_by_student(student_id: int) -> Review | None:
    reviews: Review | None = Review.query.filter_by(student_id=student_id).first()
    if not reviews:
        print(f'No reviews found for student ID [ {student_id} ]')
        return
    return reviews

def get_reviews_by_staff(staff_id: int) -> Review | None:
    reviews: Review | None = Review.query.filter_by(staff_id=staff_id).first()
    if not reviews:
        print(f'No reviews found for staff ID [ {staff_id} ]')
        return
    return reviews

def print_reviews(reviews: list[Review]) -> None:
    headers: list[str] = ["Rating", "Student", "Author", "Review Comment"]
    student_reviews: list[list[Union[str, int]]] = []
    for review in reviews:
        student_reviews.append([review.rating, review.student.student_id, review.author.staff_id, review.comment])
    print()
    print(tabulate(tabular_data=student_reviews, headers=headers, tablefmt="fancy_grid"))
    print()
