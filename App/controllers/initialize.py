import json
from .user import create_user
from .student import create_student
from .staff import create_staff
from .review import create_review
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()

    # Load seed data from JSON
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Create Students
    for student in data["students"]:
        create_student(student["student_id"], student["firstname"], student["lastname"])

    # Create Staff
    for staff in data["staff"]:
        create_staff(staff["staff_id"], staff["firstname"], staff["lastname"])

    # Create Reviews
    for review in data["reviews"]:
        create_review(review["student_id"], review["staff_id"], review["rating"], review["comment"])
