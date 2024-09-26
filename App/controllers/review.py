from App.models import Review
from App.database import db

def create_review(student_id, staff_id, is_positive, rating, comment):
    new_review = Review(
        student_id=student_id, 
        staff_id=staff_id, 
        is_positive=is_positive, 
        rating=rating, 
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    
    
def get_all_reviews():
    return Review.query.all()