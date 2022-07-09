# Connect to Database
from mysql.connector import connect, Error

# DEFINE SQL QUERIES
DB = 'newsread'
USER = 'root'
HOST = 'localhost'
CREATE_DB = 'CREATE DATABASE newsread'
SHOW_DB = 'SHOW DATABASES'
SHOW_TB = 'SHOW TABLES'
CREATE_USER_TABLE = """
CREATE TABLE user(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(20) NOT NULL UNIQUE,
password blob NOT NULL, 
email_address VARCHAR(35), NOT NULL, UNIQUE
)"""


def create_database():
    try:
        with connect(
                host=HOST,
                user=USER,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(SHOW_DB)
                dbs = [db[0] for db in cursor]
                if DB not in dbs:
                    create_db = f"CREATE DATABASE {DB}"
                    with connection.cursor() as cursor:
                        cursor.execute(create_db)
        return True
    except Error as e:
        print(e)
        return False
