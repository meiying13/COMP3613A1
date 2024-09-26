from App.database import db

class Student(db.Model):
    student_id = db.Column(db.String(8), primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, student_id, firstname, lastname):
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return f'< Student: {self.student_id} | {self.get_fullname()} | reviews [{self.get_reviews()}] >'
    
    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'
        
    def get_reviews(self):
        student_reviews = []
        for review in self.reviews:
            author = review.author.get_fullname()
            student_reviews.append([review.rating, author, review.comment])
        return student_reviews
    
    def get_overall_rating(self):
        total: float = 0
        num_reviews: int = len(self.reviews)
        if num_reviews == 0:
            return 0
        
        for review in self.reviews:
            total += review.rating
        return total / num_reviews

    def get_json(self):
        student_reviews = self.get_reviews()
        return {
            'id': self.student_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'reviews': student_reviews
        }

