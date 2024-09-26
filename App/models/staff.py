from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.String(8), unique=True, nullable=False)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    written_reviews = db.relationship('Review', backref='author', lazy=True)

    def __init__(self, staff_id, firstname, lastname):
        self.staff_id = staff_id
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return f'< Staff: {self.id} | {self.firstname} | {self.lastname} >'
    
    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'
        
    def get_written_reviews(self):
        return ', '.join([review.comment for review in self.reviews])

    def get_json(self):
        student_reviews = self.get_written_reviews()
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'written_reviews': student_reviews
        }

