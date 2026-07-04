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

        employee_details.remove(employee)

        print("Employee deleted successfully")

        break

if not found:
    print("Employee Not Found !")

if employee_details:
    print("Employee detailes-\n","-"*50)
    for employee in employee_details:
        print(f"Employee ID : {employee['emp_id']}")
        print(f"Name : {employee['emp_name']}")
        print(f"Age : {employee['age']}")
        print(f"Department : {employee['emp_department']}")
        print(f"Salary : {employee['emp_salary']:.2f}")
else:
    print("The database is empty ! Nothing to retrieve.")