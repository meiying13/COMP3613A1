from App.models import Review, Staff, Student
from App.database import db

def create_review(student_id, staff_id, rating, comment):
    staff: Staff | None = Staff.query.filter_by(staff_id=staff_id).first()
    if not staff:
        print(f'\nStaff with ID [ {staff_id} ] not found !\n')
        return
        
    student: Student | None = Student.query.filter_by(student_id=student_id).first()
    if not student:
        print(f'\nStudent with ID [ {student_id} ] not found !\n')
        return
        
    if rating < 1 or rating > 5:
        print(f'\nInvalid rating [ {rating} ]. Rating for student must be between 1 (Very Poor) and 5 (Excellent).\n')
        return
    
    new_review = Review(
        student_id=student.student_id, 
        staff_id=staff.staff_id, 
        rating=rating, 
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    print(f'\nReview for [ {student_id} | {student.get_fullname()} ] added !\n')
    
    
def get_all_reviews():
    return Review.query.all()

def get_reviews_by_student(student_id):
    reviews = Review.query.filter_by(student_id=student_id).first()
    if not reviews:
        print(f'No reviews found for student ID [ {student_id} ]')
        return
    return reviews


def get_reviews_by_staff(staff_id):
    reviews = Review.query.filter_by(staff_id=staff_id).first()
    if not reviews:
        print(f'No reviews found for staff ID [ {staff_id} ]')
        return
    return reviews