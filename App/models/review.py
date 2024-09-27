from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(8), db.ForeignKey('student.student_id'), nullable=False)
    staff_id = db.Column(db.String(8), db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    
    def __init__(self, student_id, staff_id, rating, comment):
        self.student_id = student_id
        self.staff_id = staff_id
        self.rating = rating
        self.comment = comment
        
    def __repr__(self):
        return f'< Review: {self.id} | {self.student.get_fullname()} | {self.author.get_fullname()} | {self.rating} | {self.comment}] >'
        
    def get_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'staff_id': self.staff_id,
            'rating': self.rating,
            'comment': self.comment            
        }
