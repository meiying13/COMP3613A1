# Student Conduct Tracker

Staff system for recording positive and negative experiences with students. Main features include:

1. Add Student

2. Review student

3. Search Student

4. View student reviews


# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```


# Student Management CLI Commands

This document outlines the various Flask CLI commands available for managing student data within the application.

## Commands Overview

### 1. Adding a Student

```bash
$ flask student add
```
- **Description**: This command prompts the user to input the necessary details to create a new student record in the database. Users need to authenticate as an administrator and provide a student ID, first name, and last name.

```
### Sample Output

Enter username: admin
Enter password: 
Enter Student ID: 81600613
Enter Firstname: Andrew
Enter Lastname: Garfield
Enter Programme: Master of Fine Arts in Creative Writing
Student [ 81600613 | Andrew Garfield ] added!
```

### 2. Listing All Students

```bash
$ flask student list-all
```
- **Description**: This command retrieves and displays a list of all students currently stored in the database.

```
### Sample Output

╒══════════╤════════════════════╤═════════════════════════════════════════════════════════╕
│       ID │ Name               │ Programme of Study                                      │
╞══════════╪════════════════════╪═════════════════════════════════════════════════════════╡
│ 81600000 │ James Smith        │ Bachelor of Science in Information Technology           │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600001 │ Olivia Brown       │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600002 │ Liam Johnson       │ Bachelor of Science in Information Technology (Special) │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600003 │ Emma Williams      │ Bachelor of Science in Software Engineering             │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600004 │ Mia Davis          │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600005 │ Benjamin Rodriguez │ Master of Business Administration (MBA)                 │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600006 │ El Martinez        │ Bachelor of Science in Electrical Engineering           │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600007 │ Ethan Smith        │ Bachelor of Science in Environmental Science            │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600008 │ Amelia Clark       │ Bachelor of Education in Early Childhood Education      │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600009 │ Mason Lopez        │ Bachelor of Science in Chemistry                        │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600010 │ Sophia Lee         │ Master of Science in Data Analytics                     │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600011 │ Logan Hernandez    │ Bachelor of Science in Chemistry                        │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600012 │ Ava Thompson       │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600013 │ Ella Martinez      │ Bachelor of Fine Arts in Graphic Design                 │
╘══════════╧════════════════════╧═════════════════════════════════════════════════════════╛
```

### 3. Searching for a Student by ID

```bash
$ flask student search-id
```
- **Description**: This command prompts the user for a student ID and retrieves the corresponding student record from the database. If a matching student is found, their details will be displayed.

```
### Sample Output

Enter Student ID: 81600000

STUDENT ID      -       81600000
NAME            -       James Smith
PROGRAMME       -       Bachelor of Science in Information Technology
OVERALL RATING  -       3.7 star(s) (3 reviews)
```

### 4. Searching for Students by Name

```bash
$ flask student search-name
```
- **Description**: This command allows users to search for students by their first and last name. The user is prompted to enter a first name and last name, and the command returns all students whose name match the input.

```
### Sample Output

Enter firstname: el
Enter lastname: martinez

╒══════════╤═══════════════╤═══════════════════════════════════════════════╕
│       ID │ Name          │ Programme of Study                            │
╞══════════╪═══════════════╪═══════════════════════════════════════════════╡
│ 81600006 │ El Martinez   │ Bachelor of Science in Electrical Engineering │
├──────────┼───────────────┼───────────────────────────────────────────────┤
│ 81600013 │ Ella Martinez │ Bachelor of Fine Arts in Graphic Design       │
╘══════════╧═══════════════╧═══════════════════════════════════════════════╛
```

### 5. Adding a Review for a Student

```bash
$ flask student add-review
```
- **Description**: This command prompts the user to input details for adding a review to a specific student record. Users need to authenticate as a staff member and provide a student ID, rating, and comment.

```
### Sample Output

Enter username: bob
Enter password: 

╒══════════╤════════════════════╤═════════════════════════════════════════════════════════╕
│       ID │ Name               │ Programme of Study                                      │
╞══════════╪════════════════════╪═════════════════════════════════════════════════════════╡
│ 81600000 │ James Smith        │ Bachelor of Science in Information Technology           │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600001 │ Olivia Brown       │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600002 │ Liam Johnson       │ Bachelor of Science in Information Technology (Special) │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600003 │ Emma Williams      │ Bachelor of Science in Software Engineering             │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600004 │ Mia Davis          │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600005 │ Benjamin Rodriguez │ Master of Business Administration (MBA)                 │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600006 │ El Martinez        │ Bachelor of Science in Electrical Engineering           │
╘══════════╧════════════════════╧═════════════════════════════════════════════════════════╛

Enter Student ID: 81600001
Rating (1=Very Poor, 5=Excellent): 5
Comment: Consistently shows excellent initiative and teamwork 
Review for Student [ 81600001 ] added!
```

### 6. Viewing a Student's Reviews

```bash
$ flask student view-reviews
```
- **Description**: This command prompts the user to enter a student ID and retrieves all reviews associated with that student. It displays the reviews, including ratings and comments.

```
### Sample Output

╒══════════╤════════════════════╤═════════════════════════════════════════════════════════╕
│       ID │ Name               │ Programme of Study                                      │
╞══════════╪════════════════════╪═════════════════════════════════════════════════════════╡
│ 81600000 │ James Smith        │ Bachelor of Science in Information Technology           │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600001 │ Olivia Brown       │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600002 │ Liam Johnson       │ Bachelor of Science in Information Technology (Special) │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600003 │ Emma Williams      │ Bachelor of Science in Software Engineering             │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600004 │ Mia Davis          │ Bachelor of Science in Computer Science (Special)       │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600005 │ Benjamin Rodriguez │ Master of Business Administration (MBA)                 │
├──────────┼────────────────────┼─────────────────────────────────────────────────────────┤
│ 81600006 │ El Martinez        │ Bachelor of Science in Electrical Engineering           │
╘══════════╧════════════════════╧═════════════════════════════════════════════════════════╛

Enter Student ID: 81600000

STUDENT ID      -       81600000
NAME            -       James Smith
PROGRAMME       -       Bachelor of Science in Information Technology
OVERALL RATING  -       3.7 star(s) (3 reviews)
REVIEWS         -
╒══════════╤═════════════╤═════════════════════════════════════════════════════════════════════════════════════════════╕
│   Rating │ Author      │ Review Comment                                                                              │
╞══════════╪═════════════╪═════════════════════════════════════════════════════════════════════════════════════════════╡
│        5 │ Alice Brown │ Excellent work and consistent effort throughout the semester. Always prepared and engaged.  │
├──────────┼─────────────┼─────────────────────────────────────────────────────────────────────────────────────────────┤
│        2 │ Bob Ross    │ Needs significant improvement in communication skills and teamwork.                         │
├──────────┼─────────────┼─────────────────────────────────────────────────────────────────────────────────────────────┤
│        4 │ Bob Ross    │ Shows great promise. Active participation in class but needs to polish written assignments. │
╘══════════╧═════════════╧═════════════════════════════════════════════════════════════════════════════════════════════╛
```


# Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```
