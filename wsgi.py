import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Review
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers.review import (create_review)
from App.controllers.student import (create_student, get_all_students, search_student_by_id, print_student, print_students)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')


'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


student_cli = AppGroup('student', help='Student object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@student_cli.command("add", help="Creates a student")
@click.argument("id", default="00000000")
@click.argument("firstname", default="Bob")
@click.argument("lastname", default="Ross")
def create_student_command(id, firstname, lastname):
    create_student(id, firstname, lastname)
    

@student_cli.command("review", help="Adds a review for a student")
@click.argument("student_id", default="00000000")
@click.argument("rating", default=5)
@click.argument("comment", default="Good work ethic")
def review_student_command(student_id, rating, comment):
    create_review(student_id, "00000613", rating, comment)
    

@student_cli.command("list", help="List all students")
def list_students_command():
    students = get_all_students()
    print_students(students)
    
        
@student_cli.command("get", help="Get a student and their reviews")
@click.argument("student_id", default="00000000")
def get_student_command(student_id):
    student: Student | None = search_student_by_id(student_id)
    if student:
        print_student(student)
            
    
app.cli.add_command(student_cli) # add the group to the cli

'''
Test Commands
'''

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