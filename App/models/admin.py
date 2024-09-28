from App.database import db
from .user import User

class Admin(User):
    __tablename__: str = "admin"
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
    
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username=username, password=password)

    def __repr__(self) -> str:
        return f'< Admin: {self.id} | {self.username} >'
