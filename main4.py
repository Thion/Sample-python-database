from database import School_Admin

try:
    name = input("Enter name\n")
    age = input("Enter your age\n")
    gender = input("Enter your gender\n")
    email = input("Enter email\n")
    password = input("Enter your password\n")
    School_Admin.create(name=name, age=age, gender=gender, email=email, password=password)
    print("Data saved successfully")
except:
    print("An error occurred")