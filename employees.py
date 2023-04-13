from database import Employee

employees = Employee.select()
for employee in employees:
    print(employees.name, employees.regnumber, employees.worktype)