from App.models import Staff
from App.database import db

def create_staff(staff_id, password, firstname, lastname):
    new_staff = Staff(
        staff_id=staff_id, 
        password=password,
        firstname=firstname, 
        lastname=lastname
    )
    db.session.add(new_staff)
    db.session.commit()
    
    
def get_all_staff():
    return Staff.query.all()