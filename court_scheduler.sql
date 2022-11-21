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
	date DATE NOT NULL UNIQUE
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
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(3, 1)

INSERT INTO schedule (day_of_week, date, scheduler_id, employee_id, assignment_id) VALUES 
('Monday', '2022-11-14', 1, 4, 1),
('Monday', '2022-11-14', 1, 5, 2),
('Monday', '2022-11-14', 1, 6, 3),
('Monday', '2022-11-14', 1, 7, 4),
('Monday', '2022-11-14', 1, 8, 5),
('Monday', '2022-11-14', 1, 9, 6),
('Monday', '2022-11-14', 1, 10, 7),
('Monday', '2022-11-14', 1, 11, 8),
('Monday', '2022-11-14', 1, 4, 9),
('Monday', '2022-11-14', 1, 5, 10),
('Monday', '2022-11-14', 1, 6, 12),
('Monday', '2022-11-14', 1, 7, 13);