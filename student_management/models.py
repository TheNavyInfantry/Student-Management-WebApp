from student_management import db
from student_management import date

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    university_code = db.Column(db.String(length=6), nullable=False, default='#', unique=True)
    name = db.Column(db.String(length=50), nullable=True, default='#')
    surname = db.Column(db.String(length=50), nullable=True, default='#')
    register_date = db.Column(db.String(length=10), nullable=True, default=date.today)
    faculty = db.Column(db.String(length=250), nullable=False, default='#')

    def __repr__(self):
        return f"Student ID: {self.id}\nUni Code: {self.university_code}\nName: {self.name}\n" \
               f"Surname: {self.surname}\nRegister Date: {self.register_date}\nFaculty: {self.faculty}\n----------\n"