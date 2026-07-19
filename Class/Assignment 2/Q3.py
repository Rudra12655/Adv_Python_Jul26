class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class ContractEmployee(Employee):
    def __init__(self, employee_id, name, project_amount, bonus):
        super().__init__(employee_id, name)
        self.project_amount = project_amount
        self.bonus = bonus

    def calculate_salary(self):
        return self.project_amount + self.bonus


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self):
        total_salary = 0

        for employee in self.employees:
            salary = employee.calculate_salary()

            print("Employee ID :", employee.employee_id)
            print("Name :", employee.name)
            print("Salary : ₹{}".format(salary))
            print()

            total_salary += salary

        print("Total Payroll : ₹{}".format(total_salary))




emp1 = FullTimeEmployee(101, "Anand", 60000)

emp2 = PartTimeEmployee(102, "Isha", 120, 150)

emp3 = ContractEmployee(103, "Chinmayi", 45000, 5000)

payroll = Payroll()

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

payroll.generate_payroll()