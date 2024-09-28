from App.models import Admin
from App.database import db

def create_admin(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if admin:
        print(f'Admin with username [ {username} ] already exists !')
        return
    new_admin = Admin(username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()
    print(f'Admin | {username} added !')
     

def get_admin_by_username(username):
    admin = Admin.query.filter_by(username=username).first()
    if not admin:
        print(f'Admin with username [ {username} ] not found!')
        return
    return admin

def authenticate_admin(username, password):
    admin: Admin | None = get_admin_by_username(username)
    if admin:
        return admin.check_password(password)
    return False