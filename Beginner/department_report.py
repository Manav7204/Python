employee_details = [
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

if not employee_details:
    print("No data found !")
    exit()

department_count = {}

for employee in employee_details:
    department = employee["emp_department"]

    if department in department_count:
        department_count[department] += 1
    else:
        department_count[department] = 1

for department, count in department_count.items():
    print(f"{department}: {count}")