from App.models import Review, Staff, Student
from App.database import db

def create_review(student_id, staff_id, rating, comment):
    staff: Staff | None = Staff.query.filter_by(staff_id=staff_id).first()
    if not staff:
        print(f'Staff with ID [ {staff_id} ] not found !')
        
    student: Student | None = Student.query.filter_by(student_id=student_id).first()
    if not staff:
        print(f'Student with ID [ {student_id} ] not found !')
    
    new_review = Review(
        student_id=student.student_id, 
        staff_id=staff.staff_id, 
        rating=rating, 
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    
    
def get_all_reviews():
    return Review.query.all()