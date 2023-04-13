from database import Employee

try:
    employee_name = input("Enter employee name\n")
    registration_number = input("Enter registration number\n")
    work_type = input("Enter the type of your work\n")
    Employee.create(name=employee_name, regno=registration_number, Type_of_work=work_type)
    print("Data saved successfully")
except:
    print("Error occurred")


