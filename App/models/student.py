from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)

    def __init__(self, student_id, firstname, lastname):
        self.id = student_id
        self.firstname = firstname
        self.lastname = lastname

    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

