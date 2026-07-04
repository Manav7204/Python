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

for employee in employee_details:
    print("Employee ID:", employee["emp_id"])
    print("Name:", employee["emp_name"])
    print("Age:", employee["age"])
    print("Department:", employee["emp_department"])
    print("Salary:", employee["emp_salary"])
    print("-" * 30)