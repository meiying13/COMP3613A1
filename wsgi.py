import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import Student, Staff, Admin, Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers.review import (create_review, get_all_reviews, print_reviews)
from App.controllers.student import (
    create_student, get_all_students, 
    search_student_by_id, search_student_by_name, 
    print_student, print_students, print_student_reviews
)
from App.controllers.staff import (create_staff, get_all_staff, get_staff_by_id, authenticate_staff)
from App.controllers.admin import (authenticate_admin)


app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')


# =====================================================================
# Staff Commands
# =====================================================================

staff_cli = AppGroup('staff', help='Staff object commands') 

# This command adds a staff member to the database
# flask staff create
@staff_cli.command("create", help="Creates a staff")
def create_staff_command():
    username = click.prompt(text="Enter username")
    firstname = click.prompt(text="Enter firstname")
    lastname = click.prompt(text="Enter lastname")
    password = click.prompt(text="Enter password", hide_input=True)
    create_staff(username, firstname, lastname, password)


# This command lists all staff in the database
# flask staff list
@staff_cli.command("list", help="Lists staff in the database")
def list_staff_command():
    print(get_all_staff())

app.cli.add_command(staff_cli)


# =====================================================================
# Student Commands
# =====================================================================

student_cli = AppGroup('student', help='Student object commands') 

# This command adds a student to the database
# flask student add
@student_cli.command("add", help="Creates a student")
def create_student_command():
    username = click.prompt(text="Enter username")
    password = click.prompt(text="Enter password", hide_input=True)
    if authenticate_admin(username, password):
        student_id = click.prompt(text="Enter Student ID")
        firstname = click.prompt(text="Enter Firstname")
        lastname = click.prompt(text="Enter Lastname")
        create_student(student_id, firstname, lastname)
    else:
        print("You do not have authorization to create a student")
    

# This command adds a review for a student to the database
# flask student add-review
@student_cli.command("add-review", help="Adds a review for a student")
def review_student_command():
    username = click.prompt(text="Enter username (staff ID)")
    password = click.prompt(text="Enter password", hide_input=True)
    if authenticate_staff(username, password):
        print_students(get_all_students())
        student_id = click.prompt(text="Enter Student ID")
        rating = click.prompt(text="Rating (1=Very Poor, 5=Excellent)", type=int)
        comment = click.prompt(text="Comment")
        create_review(student_id=student_id, username=username, rating=rating, comment=comment)
    else:
        print("You do not have authorization to add a student review")


# This command displays a student's reviews in the database based on ID
# flask student view-reviews
@student_cli.command("view-reviews", help="View a student's reviews")
def get_student_reviews_command():
    student_id = click.prompt(text="Enter Student ID")
    student = search_student_by_id(student_id)
    if student:
        print_student_reviews(student)


# This command lists all students in the database
# flask student list
@student_cli.command("list", help="List all students")
def list_students_command():
    students = get_all_students()
    if not students:
        print('No students found')
    else:
        print_students(students)

# This command searches for and displays a student in the database based on ID
# flask student search-id
@student_cli.command("search-id", help="Search for a student by ID")
def get_student_by_id_command():
    student_id = click.prompt(text="Enter Student ID")
    student = search_student_by_id(student_id)
    if student:
        print_student(student)


# This command searches for and displays a student in the database based on name
# flask student search-name
@student_cli.command("search-name", help="Search for a student by name")
def get_student_by_name_command():
    firstname = click.prompt(text="Enter Firstname")
    lastname = click.prompt(text="Enter Lastname")
    student = search_student_by_name(firstname, lastname)
    if student:
        print_student(student)

app.cli.add_command(student_cli)