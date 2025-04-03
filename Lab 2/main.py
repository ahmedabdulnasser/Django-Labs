from models import Employee, Manager
from database import update_employee

while True:
    print("--------------------------")
    print("Employee Management System")
    print("--------------------------")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Show Employees")
    print("4. Delete Employee")
    print("Q. Quit")
    user_input = input("Your choice: ").strip().lower()
    if user_input == "1":
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        department = input("Department: ").strip()
        try:
            age = int(input("Age: "))
            salary = int(input("Salary: "))
        except ValueError:
            print("Age and Salary must be numbers.")
            continue
        employee_role = (
            input("if manager press “m”/ if employee press ‘e’ ").strip().lower()
        )
        if employee_role == "m":
            Manager(first_name, last_name, department, age, salary)
        else:
            Employee(first_name, last_name, department, age, salary)
    elif user_input == "2":
        try:
            emp_id = int(input("Employee ID: ").strip())
        except ValueError:
            print("Employee ID must be a number.")
            continue
        if not any(emp[0] == emp_id for emp in Employee.employees):
            print(f"Employee with ID {emp_id} not found.")
            continue

        allowed_options = [
            "first_name",
            "last_name",
            "department",
            "age",
            "salary",
            "managed_department",
        ]
        print(f"Options: {allowed_options}")
        property_to_update = input("Property to update: ").strip().lower()

        if property_to_update in allowed_options:
            new_val = input("New Value: ").strip()
            if new_val == "":
                print("The new value cannot be empty.")
                continue

            if property_to_update in ["age", "salary"]:
                try:
                    new_val = int(new_val)
                except ValueError:
                    print(f"{property_to_update.capitalize()} must be a number.")
                    continue
                try:
                    update_employee(emp_id, property_to_update, new_val)
                    print(f"{property_to_update} updated for employee ID {emp_id}.")
                except Exception as e:
                    print(f"Failed to update: {e}")
        else:
            print("Invalid property.")

    elif user_input == "3":
        Employee.list_employees()

    elif user_input == "4":
        try:
            emp_id = int(input("Employee ID: ").strip())
        except ValueError:
            print("Employee ID must be a number.")
            continue
        if not any(emp[0] == emp_id for emp in Employee.employees):
            print(f"Employee with ID {emp_id} not found.")
            continue
        Employee.fireById(emp_id)
        print("Employee deleted.")
    elif user_input == "q":
        break
    else:
        print("Invalid choice.")
