from App.database import db
from .user import User
from .review import Review

class Staff(User):
    __tablename__: str = "staff"
    staff_id: int = db.Column(db.Integer, unique=True)
    firstname: str = db.Column(db.String(20))
    lastname: str = db.Column(db.String(20))
    written_reviews = db.relationship('Review', backref='author', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'staff', 
    }

    def __init__(self, staff_id: int, firstname: str, lastname: str, username: str, password: str) -> None:
        super().__init__(username=username, password=password)
        self.staff_id = staff_id
        self.firstname = firstname
        self.lastname = lastname
        
    def __repr__(self) -> str:
        return f'< Staff: {self.user.id} | {self.staff_id} | {self.get_fullname()} >'

    def get_fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'

    def get_json(self) -> dict[str, any]:
        student_reviews: list[dict[str, any]] = [review.get_json() for review in self.written_reviews]
        return {
            'id': self.id,
            'staff_id': self.staff_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'written_reviews': student_reviews
        }
