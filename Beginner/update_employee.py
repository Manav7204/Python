employee_details = []

while True:
    employee = {
        "emp_id" : int(input("Enter Employee ID: ")),
        "emp_name" : input("Enter name: "),
        "age" : int(input("Enter Employee age: ")),
        "emp_department" : input("Enter Department: "),
        "emp_salary" : float(input("Enter Salary: "))
        }

    employee_details.append(employee)

    choice = input("Add another employee ? (y/n): ")

    if choice.lower() != "y":
        break

search_id = int(input("Enter the ID of the employee: "))

found = False

for employee in employee_details:
    if employee["emp_id"] == search_id:
        found = True

        new_department = input("Enter the new department: ")
        new_salary = float(input("Enter the new salary: "))

        employee["emp_department"] = new_department
        employee["emp_salary"] = new_salary

        print("Employee updated successfully")

        print(f"Employee ID : {employee['emp_id']}")
        print(f"Name : {employee['emp_name']}")
        print(f"Age : {employee['age']}")
        print(f"Department : {employee['emp_department']}")
        print(f"Salary : {employee['emp_salary']}")
        break

if not found:
    print("Employee Not Found !")