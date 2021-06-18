from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)

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

@app.route("/", methods=['POST', 'GET'])
def index():
    # tags = ['ID', 'University Code', 'Name', 'Surname', 'Register Date','Faculty']
    # tags_of_form = ['university_code','name','surname','register_date','faculty']

    if request.method == 'POST':
        university_code = request.form['university_code']
        name = request.form['name']
        surname = request.form['surname']
        register_date = request.form['register_date']
        faculty = request.form['faculty']
        new_student = Student(university_code=university_code,name=name,
                              surname=surname,register_date=register_date,faculty=faculty)

        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect('/')

        except:
            return "There was an issue adding your data!"

    # return render_template('index.html', tags_of_form=tags_of_form, len_tags=len(tags_of_form), tags=tags, len=len(tags))
    return render_template('index.html')


@app.route("/list", methods=['GET'])
def list_all():
    students = Student.query.all()
    return render_template('student_table.html', students=students)

if __name__ == "__main__":
    app.run(debug=True)