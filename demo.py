import cx_Oracle
import traceback

conn = None

try:
    conn = cx_Oracle.connect("mouzikka/music@//localhost:11521/xe")
    print("Connected successfully to the database")
    print("Database version: ", conn.version)
    print("DB User: ", conn.username)
except cx_Oracle.DatabaseError:
    print("DB Error")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected successfully from the DB")
