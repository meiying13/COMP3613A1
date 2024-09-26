from App.database import db
from .user import User

class Staff(User):
    __tablename__ = "staff"
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    staff_id = db.Column(db.String(8), unique=True, nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    written_reviews = db.relationship('Review', backref='author', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }

    def __init__(self, firstname, lastname, staff_id, password):
        super().__init__(username=staff_id, password=password)
        self.staff_id = staff_id
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self):
        return f'<Staff: {self.staff_id} | {self.get_fullname()}>'
    
    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'

    def get_json(self):
        student_reviews = self.get_written_reviews()
        return {
            'staff_id': self.staff_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'written_reviews': student_reviews
        }
