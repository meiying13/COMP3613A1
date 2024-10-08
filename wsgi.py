from flask_migrate import Migrate
import click
from flask import Flask
from flask.cli import AppGroup
from App.database import get_migrate
from App.models import Student
from App.main import create_app
from App.controllers import (initialize)
from App.controllers.review import (create_review)
from App.controllers.student import (
    create_student, get_all_students, 
    search_student_by_id, search_student_by_name, 
    print_student, print_students, print_student_reviews
)
from App.controllers.staff import (authenticate_staff)
from App.controllers.admin import (authenticate_admin)


app: Flask = create_app()
migrate: Migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init() -> None:
    initialize()
    print('database intialized')


# =====================================================================
# Student Commands
# =====================================================================

student_cli = AppGroup('student', help='Student object commands') 

# This command adds a student to the database
# flask student add
@student_cli.command("add", help="Creates a student")
def create_student_command() -> None:
    password_hint = click.style("Tip: try username 'admin' and password 'admin'", fg='blue')
    click.echo(password_hint)
    username: str = click.prompt(text="Enter username")
    password: str = click.prompt(text="Enter password", hide_input=True)
    if authenticate_admin(username, password):
        student_id: int = click.prompt(text="Enter Student ID", type=int)
        firstname: str = click.prompt(text="Enter Firstname")
        lastname: str = click.prompt(text="Enter Lastname")
        programme: str = click.prompt(text="Enter Programme")
        if create_student(student_id, firstname, lastname, programme):
            print(f'Student [ {student_id} | {firstname} {lastname} ] added!')
    


# This command lists all students in the database
# flask student list
@student_cli.command("list-all", help="List all students")
def list_students_command() -> None:
    students: list[Student] = get_all_students()
    if not students:
        print('There are currently no students registered.')
    else:
        print_students(students)


# This command searches for and displays a student in the database based on ID
# flask student search-id
@student_cli.command("search-id", help="Search for a student by ID")
def get_student_by_id_command() -> None:
    student_id: int = click.prompt(text="Enter Student ID", type=int)
    student: Student | None = search_student_by_id(student_id)
    if student:
        print_student(student)


# This command searches for and displays a student in the database based on name
# flask student search-name
@student_cli.command("search-name", help="Search for students by name")
def get_student_by_name_command() -> None:
    firstname: str = click.prompt(text="Enter firstname")
    lastname: str = click.prompt(text="Enter lastname")
    students: list[Student] = search_student_by_name(firstname=firstname, lastname=lastname)
    if students:
        print_students(students)


# This command adds a review for a student to the database
# flask student add-review
@student_cli.command("add-review", help="Adds a review for a student")
def review_student_command() -> None:
    password_hint = click.style("Tip: try username 'bob' and password 'password'", fg='blue')
    click.echo(password_hint)
    username: str = click.prompt(text="Enter username")
    password: str = click.prompt(text="Enter password", hide_input=True)
    if authenticate_staff(username, password):
        print_students(get_all_students())
        student_id: int = click.prompt(text="Enter Student ID", type=int)
        rating: int = click.prompt(text="Rating (1=Very Poor, 5=Excellent)", type=int)
        comment: str = click.prompt(text="Comment")
        if create_review(student_id=student_id, username=username, rating=rating, comment=comment):
            print(f'Review for Student [ {student_id} ] added!')


# This command displays a student's reviews in the database based on ID
# flask student view-reviews
@student_cli.command("view-reviews", help="View a student's reviews")
def get_student_reviews_command() -> None:
    print_students(get_all_students())
    student_id: int = click.prompt(text="Enter Student ID", type=int)
    student: Student | None = search_student_by_id(student_id)
    if student:
        print_student_reviews(student)

app.cli.add_command(student_cli)