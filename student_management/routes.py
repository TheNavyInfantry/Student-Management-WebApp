from student_management import app
from flask import render_template, redirect, request
from student_management.models import Student
from student_management import db

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
            return redirect('/error')

    # return render_template('index.html', tags_of_form=tags_of_form, len_tags=len(tags_of_form), tags=tags, len=len(tags))
    return render_template('index.html')


@app.route("/list", methods=['GET'])
def list_all():
    students = Student.query.all()
    return render_template('student_table.html', students=students)

@app.route("/delete/<int:id>")
def delete(id):
    query_to_delete = Student.query.get_or_404(id)

    try:
        db.session.delete(query_to_delete)
        db.session.commit()
        return redirect('/list')

    except:
        return redirect('/error')

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    query_to_update = Student.query.get_or_404(id)

    if request.method == "POST":
        query_to_update.university_code = request.form['university_code']
        query_to_update.name = request.form['name']
        query_to_update.surname = request.form['surname']
        query_to_update.register_date = request.form['register_date']
        query_to_update.faculty = request.form['faculty']

        try:
            db.session.commit()
            return redirect('/list')

        except:
            return redirect('/error')

    else:
        return render_template('update.html', update=query_to_update)

@app.errorhandler(404)
def error_404(e):
    return render_template('404_error.html'), 404
