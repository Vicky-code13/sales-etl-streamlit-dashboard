from config.connection import DatabaseConnection


def schema_creation():
    db = DatabaseConnection()
    conn, cursor = db.connect()
    with open("database/schemas/sales.sql", "r") as file:
        query = file.read()

    cursor.execute(query)

    conn.commit() 
    db.close()
    print("Schema created successfully")