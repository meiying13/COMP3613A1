from App.database import db

class Review(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String(8), db.ForeignKey('student.student_id'), nullable=False)
    staff_id: str = db.Column(db.String(8), db.ForeignKey('user.id'), nullable=False)
    rating: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.String(255), nullable=False)
    
    def __init__(self, student_id: str, staff_id: str, rating: int, comment: str) -> None:
        self.student_id = student_id
        self.staff_id = staff_id
        self.rating = rating
        self.comment = comment
        
    def __repr__(self) -> str:
        return f'< Review: {self.id} | {self.student.get_fullname()} | {self.author.get_fullname()} | {self.rating} | {self.comment}] >'
        
    def get_json(self) -> dict[str, any]:
        return {
            'id': self.id,
            'student_id': self.student_id,
            'staff_id': self.staff_id,
            'rating': self.rating,
            'comment': self.comment            
        }
