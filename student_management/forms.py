from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, ValidationError
from wtforms.validators import Length, DataRequired
from student_management.models import Student

class StudentRegisterForm(FlaskForm):

    def validate_university_code(self, university_code_to_check):
        student = Student.query.filter_by(university_code=university_code_to_check.data).first()
        if student:
            raise ValidationError("This university code is already assigned to a student! Please try a different one!")

    university_code = StringField(label='University Code', validators=[Length(min=6, max=6), DataRequired("Please fill out University Code area!")])
    name = StringField(label='Name', validators=[DataRequired("Please fill out Name area!")])
    surname = StringField(label='Surname', validators=[DataRequired("Please fill out Surname area!")])
    register_date = DateField(label='Register Date', validators=[DataRequired("Please fill out Register Date area!")])
    faculty = StringField(label='Faculty', validators=[DataRequired("Please fill out Faculty area!")])
    submit = SubmitField(label='Submit')

class StudentUpdateForm(StudentRegisterForm):
    pass