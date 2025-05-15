from mysql.connector import Error

import mysql.connector

def connect_to_database(host="localhost", user="pare", password="pare_password", database="tapatapp"):
    """
    Connects to a MySQL database using the specified user credentials.

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
            print(f"Connected to the database as user: {user}")
            return connection
    except Error as e:
        print(f"Error connecting to database as user {user}: {e}")
        return None

def list_all_tables(connection):
    """
    Lists all tables in the connected database.

    :param connection: MySQL connection object
    """
    try:
        with connection.cursor() as cursor:
            query = "SHOW TABLES"
            cursor.execute(query)
            tables = cursor.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table[0])  # Each table name is in the first column of the result
    except Error as e:
        print(f"Error listing tables: {e}")

if __name__ == "__main__":
    # Connect to the database as user "pare"
    print("Connecting as user 'pare'...")
    conn_pare = connect_to_database(user="pare", password="pare_password")

    if conn_pare:
        # List all tables in the database
        list_all_tables(conn_pare)

        # Close the connection
        if conn_pare.is_connected():
            conn_pare.close()
            print("Database connection closed for user 'pare'.")

    # Connect to the database as user "mare"
    print("\nConnecting as user 'mare'...")
    conn_mare = connect_to_database(user="mare", password="mare_password")

    if conn_mare:
        # List all tables in the database
        list_all_tables(conn_mare)

        if conn_mare.is_connected():
            conn_mare.close()
            print("Database connection closed for user 'mare'.")
        print("Database connection closed for user 'mare'.")