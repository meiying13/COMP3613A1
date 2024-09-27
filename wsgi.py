import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import Student
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers.review import (create_review, get_all_reviews, print_reviews)
from App.controllers.student import (
    create_student, get_all_students, 
    search_student_by_id, search_student_by_name, 
    print_student, print_students, print_student_reviews
)

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')


# =====================================================================
# User Commands
# =====================================================================

user_cli = AppGroup('user', help='User object commands') 

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')


@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli)


# =====================================================================
# Student Commands
# =====================================================================

student_cli = AppGroup('student', help='Student object commands') 


# This command adds a student to the database
# flask student add [id] [firstname] [lastname]
@student_cli.command("add", help="Creates a student")
@click.argument("id", default="00000000")
@click.argument("firstname", default="Rob")
@click.argument("lastname", default="Ross")
def create_student_command(id, firstname, lastname):
    create_student(id, firstname, lastname)
    

# This command adds a review for a student to the database
# flask student add-review [id] [student_id] [rating] [comment]
@student_cli.command("add-review", help="Adds a review for a student")
@click.argument("student_id", default="00000000")
@click.argument("rating", default=5)
@click.argument("comment", default="Good work ethic")
def review_student_command(student_id, rating, comment):
    create_review(student_id, "00000613", rating, comment)
    

# This command displays a student's reviews in the database based on ID
# flask student view-reviews [id]
@student_cli.command("view-reviews", help="View a student's reviews")
@click.argument("student_id", default="00000000")
def get_student_by_id_command(student_id):
    student: Student | None = search_student_by_id(student_id)
    if student:
        print_student_reviews(student)
    

# This command displays a list of all students in the database
# flask student list
@student_cli.command("list", help="List all students")
def list_students_command():
    students = get_all_students()
    if not students:
        print('No students found')
    else:
        print_students(students)
        print_reviews(get_all_reviews())


# This command searches for and displays a student in the database based on ID
# flask student search-id [id]
@student_cli.command("search-id", help="Search for a student by ID")
@click.argument("student_id", default="00000000")
def get_student_by_id_command(student_id):
    student: Student | None = search_student_by_id(student_id)
    if student:
        print_student(student)


# This command searches for and displays a student in the database based on name
# flask student search-name [id]
@student_cli.command("search-name", help="Search for a student by name")
@click.argument("firstname", default="Rob")
@click.argument("lastname", default="Ross")
def get_student_by_name_command(firstname, lastname):
    student: Student | None = search_student_by_name(firstname, lastname)
    if student:
        print_student(student)
            
    
app.cli.add_command(student_cli)

# =====================================================================
# Test Commands
# =====================================================================

# test = AppGroup('test', help='Testing commands') 

# @test.command("user", help="Run User tests")
# @click.argument("type", default="all")
# def user_tests_command(type):
#     if type == "unit":
#         sys.exit(pytest.main(["-k", "UserUnitTests"]))
#     elif type == "int":
#         sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#     else:
#         sys.exit(pytest.main(["-k", "App"]))
    

# app.cli.add_command(test)