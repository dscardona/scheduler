from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/scheduler')
Session = sessionmaker(bind=engine)
#Base class must be inherited by each model/Python class that we want SQLAlchemy to map to a database. 
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    extension = Column(Integer, nullable=False)

    def formatted_name(self):
        return self.first_name.capitalize() + " - " + self.last_name.capitalize()


# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'first_name': 'Sara', 'last_name': 'Dowd', 'email': 'sdowd@nycourts.gov', 'extension': 8745},
    {'first_name': 'Zoraya', 'last_name': 'Echeverria', 'email': 'zecheverria@nycourts.gov', 'extension': 5544 },
    {'first_name': 'Raul', 'last_name': 'Mantilla', 'email': 'rmantilla@nycourts.gov', 'extension': 8621},
    {'first_name': 'Cheres', 'last_name': 'Espinosa', 'email': 'cespinosa@nycourts.gov', 'extension': 9965}
]


# Turn the seed data into a list of Employee objects
employee_objects = []
for item in seed_data:
    e = Employee(first_name=item["first_name"], last_name=item["last_name"], email=item["email"], extension=item["extension"])
    employee_objects.append(e)

# Create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(employee_objects)
session.commit()

# Create a new session for performing queries
session = Session()

# Run a SELECT * query on the employees table
employees = session.query(Employee).all()

for n in employees:
    print(n.first_name, n.last_name)

# SELECT * FROM employees ORDER BY first_name, email
employees = session.query(Employee).order_by(
    Employee.first_name, Employee.email).all()

for index, e in enumerate(employees):
    print(str(index+1) + ". " + e.formatted_name())