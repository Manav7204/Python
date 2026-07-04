emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter name: ")
age = int(input("Enter Employee age: "))
emp_department = input("Enter Department: ")
emp_salary = float(input("Enter Salary: "))

if age < 18:
    print("Employee is not eligible.\nReason: Minimum age requirement is 18 years.")
elif(emp_salary<15000):
    print("Employee is not eligible.\nReason: Salary is below company policy.")
else:
    print("Employee verified successfully.")
    print("\n\n_Employee Details_")
    print("\n------------------")
    print(f"Employee ID = {emp_id}")
    print(f"Employee Name = {emp_name}")
    print(f"Employee Age = {age}")
    print(f"Employee Department = {emp_department}")
    print(f"Employee Salary = {emp_salary}")