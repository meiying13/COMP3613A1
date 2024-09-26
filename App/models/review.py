from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    is_positive = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    
    def __init__(self, student_id, is_positive, rating, comment):
        self.student_id = student_id
        self.is_positive = is_positive
        self.rating = rating
        self.comment = comment
        
    def __repr__(self):
        return f'< Review: {self.id} | {self.student.get_fullname} | {"positive" if self.is_positive else "negative"} | {self.rating} | {self.comment}] >'
        
    def get_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'is_positive': self.is_positive,
            'rating': self.rating,
            'comment': self.comment            
        }
