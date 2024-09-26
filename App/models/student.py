from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    reviews = db.relationship('Review', db.backref('student', lazy=True))

    def __init__(self, student_id, firstname, lastname):
        self.id = student_id
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return f'< Student: {self.id} | {self.firstname} | {self.lastname} | reviews [{self.get_reviews()}] >'
        
    def get_reviews(self):
        return ', '.join([review.comment for review in self.reviews])

    def get_json(self):
        student_reviews = self.get_reviews()
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'reviews': student_reviews
        }

