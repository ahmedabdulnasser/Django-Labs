from database import (
    add_employee,
    delete_employee,
    get_employees,
    update_employee,
)


class Employee:
    employees = get_employees()

    @staticmethod
    def list_employees():
        for employee in Employee.employees:
            print(employee)

    @staticmethod
    def fireById(emp_id):
        employee_to_remove = next(
            (emp for emp in Employee.employees if emp[0] == emp_id), None
        )
        if employee_to_remove:
            delete_employee(emp_id)
            Employee.employees.remove(employee_to_remove)

    @staticmethod
    def transferById(emp_id, new_dept):
        update_employee(emp_id, "department", new_dept)

    def __init__(self, first_name, last_name, department, age=0, salary=6000):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
        self.salary = salary
        self.id = len(Employee.employees) + 1
        Employee.employees.append(self)
        add_employee(self.id, first_name, last_name, department, age, salary)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.department}, {self.age}, {self.salary}"

    def transfer(self, new_dept):
        self.department = new_dept
        update_employee(self.id, "department", new_dept)

    def show(self):
        print(self)

    def fire(self):
        Employee.employees.remove(self)
        delete_employee(self.id)


class Manager(Employee):
    def __init__(self, first_name, last_name, department, age=0, salary=6000):
        super().__init__(first_name, last_name, department, age, salary)
        self.managed_department = department
        update_employee(self.id, "managed_department", self.managed_department)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.department}, {self.age}, 'Confidential', Managing {self.managed_department}"

    def show(self):
        print(self)


# employee_1 = Employee("Alice", "Johnson", "Engineering", 28, 7500)
# employee_2 = Employee("Bob", "Smith", "Marketing", 35, 6800)
# employee_3 = Employee("Charlie", "Brown", "Finance", 40, 7200)
# employee_4 = Employee("David", "Williams", "HR", 30, 6400)
# employee_6 = Employee("Emma", "Davis", "IT", 26, 7000)

# Employee.transferById(3, "IT")
# Employee.fireById(3)
# mgr2 = Manager("Nash", "Ash", "HR", 22)
# Employee.transferById(2, "ARM")
# print(mgr1)
# Employee.list_employees()
