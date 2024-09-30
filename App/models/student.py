from typing import Literal
from App.database import db
from .review import Review

class Student(db.Model):
    student_id: int = db.Column(db.Integer, primary_key=True)
    firstname: str =  db.Column(db.String(20), nullable=False)
    lastname: str = db.Column(db.String(20), nullable=False)
    programme: str = db.Column(db.String(120), nullable=False)
    reviews = db.relationship('Review', backref='student', lazy=True)

    def __init__(self, student_id: int, firstname: str, lastname: str, programme: str) -> None:
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.programme = programme
        
    def __repr__(self) -> str:
        return f'< Student: {self.student_id} | {self.get_fullname()} | {self.programme} >'
    
    def get_fullname(self) -> str:
        return f'{self.firstname} {self.lastname}'
        
    
    def get_overall_rating(self) -> float:
        total: float = 0
        num_reviews: int = len(self.reviews)
        if num_reviews == 0:
            return 0
        for review in self.reviews:
            total += review.rating
        return total / num_reviews

    def get_json(self) -> dict[str, any]:
        student_reviews: list[dict[str, any]] = [review.get_json() for review in self.reviews]
        return {
            'id': self.student_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'programme': self.programme,
            'reviews': student_reviews
        }

