import json

def store_data(task_list):
    
    with open("data/task.json", "w") as file:
        json.dump(task_list, file, indent=4)

    print("Updated the json file !")

def read_data():
    try:
        with open("data/task.json", "r") as file:
            task_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No file exists!")
        return []
    
    return task_list
