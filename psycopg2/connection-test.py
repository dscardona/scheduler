#interact with POstgres database using Python database adapter psycopg2 in raw SQL.
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=scheduler user=postgres host=localhost port=5432
    """
)

conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS schedulers
    """
)

cur.execute(
    """
    CREATE TABLE schedulers(
        id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE
    )
    """
)

cur.execute(
    """
    INSERT INTO schedulers VALUES 
    (1, 'Laura', 'Avila', 'lavtest@courts.gov', 'password1', 'LAvil'),
    (2, 'Shirley', 'Landberg', 'slandtest@courts.gov', 'password2', 'SLand'),
    (3, 'Rene', 'Medina', 'rmedi@courts.gov', 'password3', 'RMed')
    """
)

# Execute a query
cur.execute(
    """
    SELECT * FROM schedulers
    """
)

# Retrieve query results
records = cur.fetchall()

# print(records)

cur.execute(
    """
    SELECT first_name, last_name FROM schedulers
    """
)

admin_names = cur.fetchall()
for n in admin_names:
    print(n[0], n[1])


print('')  # new line

cur.execute(
    """
    SELECT first_name, last_name FROM schedulers ORDER BY last_name
    """
)

admin_names = cur.fetchall()

for count, name in enumerate(admin_names):
    print(str(count+1) + ".", name[0].capitalize(), name[1].capitalize())