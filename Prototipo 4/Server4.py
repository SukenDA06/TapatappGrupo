import mysql.connector
from mysql.connector import Error

def connect_to_database(host="localhost", user="root", password="root", database="tapatapp"):
    """
    Connects to a MySQL database.

    :param host: Hostname of the database server
    :param user: Username for the database
    :param password: Password for the database
    :param database: Name of the database
    :return: Connection object
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Connected to the database: {database}")
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def list_all_tables(connection):
    """
    Lists all tables in the connected database.

    :param connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        query = "SHOW TABLES"
        cursor.execute(query)
        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table[0])  # Each table name is in the first column of the result
    except Error as e:
        print(f"Error listing tables: {e}")

if __name__ == "__main__":
    # Connect to the MySQL database
    conn = connect_to_database()

    if conn:
        # List all tables in the database
        list_all_tables(conn)

        # Close the connection
        conn.close()
        print("Database connection closed.")