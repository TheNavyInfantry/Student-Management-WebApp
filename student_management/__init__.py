from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SECRET_KEY'] = '52f66d9364665810978000d1'
db = SQLAlchemy(app)

from student_management import routes