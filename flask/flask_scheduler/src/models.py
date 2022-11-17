from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scheduler(db.Model):
    __tablename__ = 'schedulers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128), nullable=False)

employees_days_off_table = db.Table(
    'employees_days_off',
    db.Column(
        'employee_id', db.Integer,
        db.ForeignKey('employees.id'),
        primary_key=True
    ),

    db.Column(
        'day_off_id', db.Integer,
        db.ForeignKey('days_off.id'),
        primary_key=True
    ),
)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    extension = db.Column(db.Integer, nullable=False)
    days_off = db.relationship('Day_off', secondary=employees_days_off_table, lazy='subquery', backref=db.backref('employees', lazy=True))


class Day_off(db.Model):
    __tablename__ = 'days_off'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day_of_week = db.Column(db.String(28), nullable=False)
    date = db.Column(db.String(28), nullable=False, unique=True)
    user_taking_off = db.relationship('Employee', secondary=employees_days_off_table)


schedule_table = db.Table(
    'schedule',
    db.Column(
        'date', db.String,
        primary_key=True
    ),

    db.Column(
        'day_of_week', db.String,
        nullable=False
    ),

    db.Column(
        'scheduler_id', db.Integer,
        db.ForeignKey('schedulers.id'),
        nullable=False
    ),

    db.Column(
        'employee_id', db.Integer,
        db.ForeignKey('employees.id'),
        primary_key=True
    ),

    db.Column(
        'assignment_id', db.Integer,
        db.ForeignKey('assignments.id'),
        primary_key=True
    ),
)
