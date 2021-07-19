from student_management import app
from flask import render_template, redirect, url_for, request, flash
from student_management.models import Student
from student_management.forms import StudentRegisterForm, StudentUpdateForm
from student_management import db

@app.route("/", methods=['POST', 'GET'])
def index():

    form = StudentRegisterForm()

    if form.validate_on_submit():
        new_student = Student(university_code=form.university_code.data, name=form.name.data,
                              surname=form.surname.data, register_date=form.register_date.data,
                              faculty=form.faculty.data)

        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('index'))

        except:
            return redirect(url_for('error_404'))

    if form.errors != {}: #Means if there are not errors from the validations
        for error_msg in form.errors.values():
            flash(f'There was an error: {error_msg}', category='warning')

    return render_template('index.html', form=form)


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
        return redirect(url_for('list_all'))

    except:
        return redirect(url_for('error_404'))

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
            return redirect(url_for('list_all'))

        except:
            return redirect(url_for('error_404'))

    else:
        return render_template('update.html', update=query_to_update)

@app.errorhandler(404)
def error_404(e):
    return render_template('404_error.html'), 404
