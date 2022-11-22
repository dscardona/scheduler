from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

class Scheduler(db.Model):
    __tablename__ = 'schedulers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    shift_scheduled_association = db.relationship('Schedule', back_populates='scheduler')
    shifts_scheduled = association_proxy("shift_scheduled_association", "scheduler")

class Assignment(db.Model):
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(128), nullable=False)
    assigned_to_association = db.relationship('Schedule', back_populates='assignment')
    assigned_to = association_proxy("assigned_to_association", "assignment")

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
    days_off = db.relationship('Day_off', secondary=employees_days_off_table, lazy='True', backref="unavailable_employees")
    assigned_association = db.relationship('Schedule', back_populates='employee')
    assigned = association_proxy("assigned_association", "employee")

class Day_off(db.Model):
    __tablename__ = 'days_off'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day_of_week = db.Column(db.String(28), nullable=False)
    date = db.Column(db.String(28), nullable=False, unique=True)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column('date', db.String, nullable=False)
    day_of_week = db.Column('day_of_week', db.String, nullable=False)
    scheduler_id = db.Column('scheduler_id', db.Integer, db.ForeignKey('schedulers.id'), nullable=False)
    employee_id = db.Column('employee_id', db.Integer, db.ForeignKey('employees.id'))
    assignment_id = db.Column('assignment_id', db.Integer, db.ForeignKey('assignments.id'))

    scheduler = db.relationship('Scheduler', back_populates='shift_scheduled_association')
    employee = db.relationship('Scheduler', back_populates='assigned_association')
    assignment = db.relationship('Scheduler', back_populates='assigned_to_association')
    



