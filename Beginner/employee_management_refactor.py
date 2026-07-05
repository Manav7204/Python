# GET DATA -
def get_employee_data():
    
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
    
    return employee_details

# Display Employees -
def display_employees(employee_details):
    for employee in employee_details:
        print("Employee ID:", employee["emp_id"])
        print("Name:", employee["emp_name"])
        print("Age:", employee["age"])
        print("Department:", employee["emp_department"])
        print("Salary:", employee["emp_salary"])
        print("-" * 30)

# Summary of Employees -
def employee_summary(employee_data):
    if not employee_data:
        print("No employee data found !")

    total_employees = len(employee_data)

    total_salary = employee_data[0]["emp_salary"]

    highest_employees = [employee_data[0]]
    highest_salary = employee_data[0]["emp_salary"]

    lowest_employees = [employee_data[0]]
    lowest_salary = employee_data[0]["emp_salary"]

    for employee in employee_data[1:]:

        total_salary += employee["emp_salary"]

        if employee["emp_salary"] > highest_salary:
            highest_salary = employee["emp_salary"]
            highest_employees = [employee]
        elif employee["emp_salary"] == highest_salary:
            highest_employees.append(employee)

        if employee["emp_salary"] < lowest_salary:
            lowest_salary = employee["emp_salary"]
            lowest_employees = [employee]
        elif employee["emp_salary"] == lowest_salary:
            lowest_employees.append(employee)

    avg_salary = total_salary/total_employees


    print("="*15, "Employee summary", "="*15)
    print("-"*45)
    print(f"{'Total Employees':<16} : {total_employees}")
    print(f"{'Total Salary':<16} : ₹{total_salary:.2f}")
    print(f"{'Average Salary':<16} : ₹{avg_salary:.2f}")

# Search data -
def search_employee(employee_details):
    search_id = int(input("Enter the ID of the employee: "))
    found = False

    for employee in employee_details:
        if employee["emp_id"] == search_id:
            found = True
            print(f"Employee ID : {employee['emp_id']}")
            print(f"Name : {employee['emp_name']}")
            print(f"Age : {employee['age']}")
            print(f"Department : {employee['emp_department']}")
            print(f"Salary : {employee['emp_salary']}")
            break

    if not found:
        print("Not Found !")

# Delete Employee -
def delete_employee(employee_details):
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

# Update employee data -
def update_employee(employee_details):
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

            break

    if not found:
        print("Employee Not Found !")

# Report -
def employee_report(employee_details):
    if not employee_details:
        print("No data found !")

    department_count = {}

    for employee in employee_details:
        department = employee["emp_department"]

        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

    for department, count in department_count.items():
        print(f"{department}: {count}")

employee_details = get_employee_data()
display_employees(employee_details)
employee_summary(employee_details)
search_employee(employee_details)
delete_employee(employee_details)
update_employee(employee_details)
employee_report(employee_details)
