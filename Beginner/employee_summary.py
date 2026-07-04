# def get_employee_data():
    
#     employee_details = []

#     while True:
#         employee = {
#             "emp_id" : int(input("Enter Employee ID: ")),
#             "emp_name" : input("Enter name: "),
#             "age" : int(input("Enter Employee age: ")),
#             "emp_department" : input("Enter Department: "),
#             "emp_salary" : float(input("Enter Salary: "))
#         }

#         employee_details.append(employee)

#         choice = input("Add another employee ? (y/n): ")

#         if choice.lower() != "y":
#             break
    
#     return employee_details

# employee_data = get_employee_data()
employee_data = [
    {
        "emp_id": 101,
        "emp_name": "Manav",
        "age": 22,
        "emp_department": "Backend",
        "emp_salary": 45000.00
    },
    {
        "emp_id": 102,
        "emp_name": "Rahul",
        "age": 24,
        "emp_department": "AI",
        "emp_salary": 70000.00
    },
    {
        "emp_id": 103,
        "emp_name": "Priya",
        "age": 23,
        "emp_department": "Backend",
        "emp_salary": 55000.00
    },
    {
        "emp_id": 104,
        "emp_name": "Aman",
        "age": 25,
        "emp_department": "Testing",
        "emp_salary": 35000.00
    },
    {
        "emp_id": 105,
        "emp_name": "Neha",
        "age": 26,
        "emp_department": "HR",
        "emp_salary": 30000.00
    },
    {
        "emp_id": 106,
        "emp_name": "Karan",
        "age": 27,
        "emp_department": "Backend",
        "emp_salary": 70000.00
    },
    {
        "emp_id": 107,
        "emp_name": "Sneha",
        "age": 21,
        "emp_department": "AI",
        "emp_salary": 28000.00
    },
    {
        "emp_id": 108,
        "emp_name": "Rohit",
        "age": 29,
        "emp_department": "Testing",
        "emp_salary": 35000.00
    }
]

if not employee_data:
    print("No employee data found !")
    exit()

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

print("Highest Paid Employees")
for employee in highest_employees:
    print(f"{employee['emp_name']} - ₹{employee['emp_salary']:.2f}")

print("Lowest Paid Employees")
for employee in lowest_employees:
    print(f"{employee['emp_name']} - ₹{employee['emp_salary']:.2f}")