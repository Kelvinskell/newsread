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
username VARCHAR(20) UNIQUE NOT NULL,
password VARCHAR(10000) NOT NULL, 
email_address VARCHAR(35) UNIQUE NOT NULL
)"""


def create_database():
    # Connect to Database
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

def create_table():
    with connect(
            host=HOST,
            user=USER,
            database=DB,
            ) as connection:
        with connection.cursor() as cursor:

            # Get existing Tables
            with connection.cursor() as cursor:
                cursor.execute(SHOW_TB)
                tbs = [tb[0] for tb in cursor]

                # Create Table
                if 'user' not in tbs:
                    cursor.execute(CREATE_USER_TABLE)
                    connection.commit()
        
        

