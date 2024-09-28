from typing import Any
from App.models import User
from App.database import db

def create_user(username, password) -> User:
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_username(username) -> User | None:
    return User.query.filter_by(username=username).first()

def get_user(id) -> User | None:
    return User.query.get(id)

def get_all_users() -> list[User]:
    return User.query.all()

def get_all_users_json() -> list[Any]:
    users: list[User] = User.query.all()
    if not users:
        return []
    users: list[Any] = [user.get_json() for user in users]
    return users

def update_user(id, username) -> User | None:
    user: User | None = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    