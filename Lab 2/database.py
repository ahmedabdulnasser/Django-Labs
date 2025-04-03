import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "employee_mgmt_db_py",
}


def create_database():
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"], user=DB_CONFIG["user"], password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_CONFIG["database"]}')
    conn.close()


def connect_db():
    return mysql.connector.connect(**DB_CONFIG)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            department VARCHAR(255) NOT NULL,
            age INT DEFAULT 0,
            salary FLOAT DEFAULT 6000,
            managed_department VARCHAR(255) NULL  
        )
    """
    )
    conn.commit()
    conn.close()


def add_employee(
    id, first_name, last_name, department, age=0, salary=6000, managed_department=None
):
    conn = connect_db()
    cursor = conn.cursor()
    sql = """
        INSERT INTO employees (id, first_name, last_name, department, age, salary, managed_department)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql, (id, first_name, last_name, department, age, salary, managed_department)
    )
    conn.commit()
    conn.close()


def get_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees


def delete_employee(id):
    conn = connect_db()
    cursor = conn.cursor()
    sql = "DELETE FROM employees WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()


def update_employee(id, property, new_val):
    conn = connect_db()
    cursor = conn.cursor()
    sql = f"UPDATE employees SET {property} = %s WHERE id = %s"
    cursor.execute(sql, (new_val, id))
    conn.commit()
    conn.close()


create_database()
create_table()
