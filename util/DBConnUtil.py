import mysql.connector as sql
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            properties = DBPropertyUtil.get_connection_properties()
            connection = sql.connect(**properties)
            return connection
        except sql.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

try:
    connection_string = DBPropertyUtil.get_connection_properties()

    connection = DBConnUtil.get_connection()


except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection if it exists
    if connection.is_connected():
        connection.close()
        print("Connected.")
