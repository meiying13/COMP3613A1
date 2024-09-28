from App.database import db
from .user import User

class Admin(User):
    __tablename__ = "admin"
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
    
    def __init__(self, username, password):
        super().__init__(username=username, password=password)

    def __repr__(self):
        return f'< Admin: {self.id} | {self.username} >'
