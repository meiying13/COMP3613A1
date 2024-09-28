from App.models import Admin
from App.database import db


def create_admin(username: str, password: str) -> bool:
    admin: Admin | None = Admin.query.filter_by(username=username).first()
    if admin:
        print(f'Admin with username [ {username} ] already exists !')
        return False
    new_admin = Admin(username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()
    return True


def get_admin_by_username(username: str) -> Admin | None:
    admin: Admin | None = Admin.query.filter_by(username=username).first()
    if not admin:
        print(f'Admin with username [ {username} ] not found!')
        return None
    return admin


def authenticate_admin(username: str, password: str) -> bool:
    admin: Admin | None = get_admin_by_username(username)
    if admin:
        if admin.check_password(password):
            return True
        print(f'Invalid password for admin [ {username} ]')
    return False
