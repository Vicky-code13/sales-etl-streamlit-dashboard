import mysql.connector
from config.settings import TARGET_DB_CONFIG


class DatabaseConnection:
    def __init__(self):
        self.config = TARGET_DB_CONFIG
        self.conn = None
        self.cursor = None

    
    def connect(self):
        try:
            if self.conn == None:
                self.conn = mysql.connector.connect(**self.config)
                self.cursor = self.conn.cursor(dictionary=True)
                print("Database is connected")
        except mysql.connector.Error as err:
            print(f"Database connection failed: {err}")
            raise
        return self.conn, self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()