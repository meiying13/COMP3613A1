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

### 2. Listing All Students

```bash
$ flask student list
```
- **Description**: This command retrieves and displays a list of all students currently stored in the database.
```python
╒══════════╤══════════════════╕
│       ID │ Name             │
╞══════════╪══════════════════╡
│ 81600000 │ John Doe         │
├──────────┼──────────────────┤
│ 81600001 │ Jane Smith       │
├──────────┼──────────────────┤
│ 81600002 │ Emily Johnson    │
├──────────┼──────────────────┤
│ 81600003 │ Michael Williams │
├──────────┼──────────────────┤
│ 81600004 │ Alice Johnson    │
├──────────┼──────────────────┤
│ 81600005 │ John Doe         │
├──────────┼──────────────────┤
│ 81600006 │ Emily Doe        │
├──────────┼──────────────────┤
│ 81600007 │ Michael Brown    │
├──────────┼──────────────────┤
│ 81600008 │ Jane Smith       │
├──────────┼──────────────────┤
│ 81600009 │ Emily Johnson    │
├──────────┼──────────────────┤
│ 81600010 │ Andrew Garfield  │
╘══════════╧══════════════════╛
```

### 3. Searching for a Student by ID

```bash
$ flask student search-id
```
- **Description**: This command prompts the user for a student ID and retrieves the corresponding student record from the database. If a matching student is found, their details will be displayed.

### 4. Searching for Students by Name

```bash
$ flask student search-name
```
- **Description**: This command allows users to search for students by their first and last name. The user is prompted to enter a first name and last name, and the command returns all students whose name match the input.

### 5. Adding a Review for a Student

```bash
$ flask student add-review
```
- **Description**: This command prompts the user to input details for adding a review to a specific student record. Users need to authenticate as a staff member and provide a student ID, rating, and comment.

### 6. Viewing a Student's Reviews

```bash
$ flask student view-reviews
```
- **Description**: This command prompts the user to enter a student ID and retrieves all reviews associated with that student. It displays the reviews, including ratings and comments.


# Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```