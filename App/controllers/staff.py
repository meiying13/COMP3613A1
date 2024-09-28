from App.models import Staff
from App.database import db


def create_staff(staff_id: str, username: str, password: str, firstname: str, lastname: str) -> bool:
    staff: Staff | None = Staff.query.filter_by(staff_id=staff_id).first()
    if staff:
        print(f'The staff ID [ {staff_id} ] already exists!')
        return False
    new_staff = Staff(
        staff_id=staff_id,
        username=username, 
        password=password,
        firstname=firstname, 
        lastname=lastname
    )
    db.session.add(new_staff)
    db.session.commit()
    return True

def get_all_staff() -> list[Staff]:
    return Staff.query.all()

def get_staff_by_id(staff_id: str) -> Staff | None:
    staff: Staff | None = Staff.query.filter_by(staff_id=staff_id).first()
    if not staff:
        print(f'Staff with ID [ {staff_id} ] not found!')
        return None
    return staff

def authenticate_staff(staff_id: str, password: str) -> bool:
    staff: Staff | None = get_staff_by_id(staff_id)
    if staff:
        if staff.check_password(password):
            return True
        print('Invalid password!')
        return False
    print(f'Staff with ID [ {staff_id} ] not found!')
    return False
