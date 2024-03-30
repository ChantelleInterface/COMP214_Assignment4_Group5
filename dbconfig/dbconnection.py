import cx_Oracle
import db

connection = None
try:
    connection = cx_Oracle.connect(
        db.username,
        db.password,
        db.dsn,
        encoding=db.encoding
    )
    print(f"Connected to Oracle Database (version {connection.version})")
except cx_Oracle.Error as error:
    print(f"Error: {error}")
finally:
    if connection:
        connection.close()
        

# Test Database Connection
with cx_Oracle.connect(
    db.username,
    db.password,
    db.dsn,
    encoding=db.encoding
) as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT 'Connected successfully!' FROM dual")
    result = cursor.fetchone()
    print(result[0])

