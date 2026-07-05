def read_data():
    try:
        with open("employee_data.txt", mode="r") as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print("File does not exist.")

def write_data(data):

    with open("employee_data.txt", mode="w") as file:
        file.write(str(data) + "\n")
    
        print("Data Saved successfully")

def add_data(data):

    with open("employee_data.txt", mode="a") as file:
        file.write(str(data) + "\n")
    
        print("Data Saved successfully")

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

write_data(employee_details)

print("written:")
read_data()

new_data = [
    {
        "emp_id": 101,
        "emp_name": "Manav",
        "age": 22,
        "emp_department": "Backend",
        "emp_salary": 45000.00
    }
]
add_data(new_data)

print("Appended: ")
read_data()