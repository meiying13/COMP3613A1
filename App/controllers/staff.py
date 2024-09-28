from App.models import Staff
from App.database import db

def create_staff(staff_id, password, firstname, lastname):
    staff = Staff.query.filter_by(staff_id=staff_id).first()
    if staff:
        print(f'The staff ID [ {staff_id} ] already exists !')
        return
    new_staff = Staff(
        staff_id=staff_id, 
        password=password,
        firstname=firstname, 
        lastname=lastname
    )
    db.session.add(new_staff)
    db.session.commit()
    print(f'{staff_id} | {firstname} {lastname} added !')
        
    
def get_all_staff():
    return Staff.query.all()


def get_staff_by_id(staff_id):
    staff = Staff.query.filter_by(staff_id=staff_id).first()
    if not staff:
        print(f'Staff with ID [ {staff_id} ] not found!')
        return
    return staff


def authenticate_staff(staff_id, password):
    staff: Staff | None = get_staff_by_id(staff_id)
    if staff:
        return staff.check_password(password)
    return False