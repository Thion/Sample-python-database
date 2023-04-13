from database import School_Admin

school_admin = School_Admin.select()
for students in School_Admin:
    print(School_Admin.name, School_Admin.age, School_Admin.gender, School_Admin.email, School_Admin.password)