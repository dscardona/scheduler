CREATE TABLE schedulers (
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	username TEXT NOT NULL UNIQUE
);

CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	extension INT NOT NULL
);

CREATE TABLE assignments (
	id SERIAL PRIMARY KEY,
	description TEXT NOT NULL
);

CREATE TABLE days_off (
	id SERIAL PRIMARY KEY,
	day_of_week TEXT NOT NULL,
	date DATE NOT NULL
);

CREATE TABLE employees_days_off (
	employee_id INT NOT NULL,
	day_off_id INT NOT NULL,
	PRIMARY KEY (employee_id, day_off_id)
);

CREATE TABLE schedule (
	date DATE NOT NULL,
	day_of_week TEXT NOT NULL,
	scheduler_id INT NOT NULL,
	employee_id INT NOT NULL,
	assignment_id TEXT NOT NULL,
	PRIMARY KEY (date, employee_id, assignment_id)
);

ALTER TABLE schedule
ADD CONSTRAINT fk_schedule_schedulers
FOREIGN KEY (scheduler_id)
REFERENCES schedulers;

ALTER TABLE schedule
ADD CONSTRAINT fk_schedule_employees
FOREIGN KEY (employee_id)
REFERENCES employees;

ALTER TABLE schedule
ADD CONSTRAINT fk_schedule_assignments
FOREIGN KEY (assignment_id)
REFERENCES assignments;

ALTER TABLE employees_days_off
ADD CONSTRAINT fk_employees_days_off_employees
FOREIGN KEY (employee_id)
REFERENCES employees;

ALTER TABLE employees_days_off
ADD CONSTRAINT fk_employees_days_off_days_off
FOREIGN KEY (day_off_id)
REFERENCES days_off;


INSERT INTO schedulers (first_name, last_name, email, password, username) VALUES 
('Laura', 'Avila', 'lavtest@courts.gov', 'password1', 'LAvil'),
('Shirley', 'Landberg', 'slandtest@courts.gov', 'password2', 'SLand'),
('Rene', 'Medina', 'rmedi@courts.gov', 'password3', 'RMed');

INSERT INTO employees (first_name, last_name, email, extension) VALUES
('Sandro', 'Tomasi', 'htomasi@nycourts.gov', 4545),
('Alejandro', 'Castro', 'acastro@nycourts.gov', 5451),
('Shirley', 'Landberg', 'slandberg@nycourts.gov', 5454),
('Cynthia', 'Viau', 'cviau@nycourts.gov', 4154),
('Glenys', 'Saldana', 'gsaldana@nycourts.gov', 1144),
('Julio', 'Rosa', 'jrosa@nycourts.gov', 8585),
('Richard', 'Blackmore', 'rblackmore@nycourts.gov', 4444),
('Sara', 'Dowd', 'sdowd@nycourts.gov', 8745),
('Zoraya', 'Echeverria', 'zecheverria@nycourts.gov', 5544 ),
('Raul', 'Mantilla', 'rmantilla@nycourts.gov', 8621),
('Cheres', 'Espinosa', 'cespinosa@nycourts.gov', 9965);

INSERT INTO assignments (description) 
VALUES
('Arraignments'), ('DAT'), ('AP2'), ('AP3'), ('AP4'),
('AP5'), ('FA'), ('FB'), ('FC'), ('TP2/TP3'), ('TP4/TP5'),
('Window'), ('Admin'), ('Translation'), ('Clerical'), ('Other');

INSERT INTO days_off (day_of_week, date) VALUES 
('Monday', '2022-11-14'),
('Tuesday', '2022-11-15'),
('Wednesday', '2022-11-16'),
('Monday', '2022-11-14'),
('Tuesday', '2022-11-15'),
('Monday', '2022-11-14');

INSERT INTO employees_days_off(employee_id, day_off_id) VALUES
(34, 14),
(34, 15),
(34, 16),
(35, 14),
(35, 15),
(36, 14);

INSERT INTO schedule (day_of_week, date, scheduler_id, employee_id, assignment_id) VALUES 
('Monday', '2022-11-14', 10, 37, 49),
('Monday', '2022-11-14', 10, 38, 50),
('Monday', '2022-11-14', 10, 39, 51),
('Monday', '2022-11-14', 10, 40, 52),
('Monday', '2022-11-14', 10, 41, 53),
('Monday', '2022-11-14', 10, 42, 54),
('Monday', '2022-11-14', 10, 43, 55),
('Monday', '2022-11-14', 10, 44, 56),
('Monday', '2022-11-14', 10, 37, 57),
('Monday', '2022-11-14', 10, 38, 58),
('Monday', '2022-11-14', 10, 39, 59),
('Monday', '2022-11-14', 10, 40, 60);