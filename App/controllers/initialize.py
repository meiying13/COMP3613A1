import csv
from .user import create_user
from .student import create_student
from .staff import create_staff
from .admin import create_admin
from .review import create_review
from App.database import db

def initialize() -> None:
    db.drop_all()
    db.create_all()
    
    # Load seed data from CSV files
    with open('data/students.csv') as students_file:
        reader = csv.DictReader(students_file)
        for row in reader:
            create_student(int(row["student_id"]), row["firstname"], row["lastname"], row["programme"])

    with open('data/staff.csv') as staff_file:
        reader = csv.DictReader(staff_file)
        for row in reader:
            create_staff(int(row["staff_id"]), row["username"], row["password"], row["firstname"], row["lastname"])
            
    with open('data/admins.csv') as admins_file:
        reader = csv.DictReader(admins_file)
        for row in reader:
            create_admin(row["username"], row["password"])

    with open('data/reviews.csv') as reviews_file:
        reader = csv.DictReader(reviews_file)
        for row in reader:
            create_review(row["student_id"], row["staff_id"], int(row["rating"]), row["comment"])
