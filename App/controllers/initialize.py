from .user import create_user
from .student import create_student
from .staff import create_staff
from .review import create_review
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    
    # Create Student
    create_student("81600000", "John", "Doe")
    create_student("81600001", "Jane", "Smith")

    # Create Staff
    create_staff("00000611", "Alice", "Brown")
    create_staff("00000612", "Bob", "Miller")

    # Create Reviews
    create_review("81600000", "00000611", is_positive=True, rating=5, comment="Excellent performance!")
    create_review("81600000", "00000612", is_positive=False, rating=2, comment="Needs improvement in communication.")
    create_review("81600001", "00000611", is_positive=True, rating=4, comment="Good student, works hard.")
    create_review("81600001", "00000612", is_positive=False, rating=3, comment="Satisfactory but can do better.")
    
    
    
    
