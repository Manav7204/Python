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

def search_task(task_list):
    
    if task_list:
        keyword = input("Enter the search word: ").strip().lower()

        if not keyword:
            print("Keyword cannot be empty.")
            return
        
        match_list = []

        for task in task_list:
            task["title"]

            if keyword in  (task["title"]).lower():
                match_list.append(task)

        if match_list:        
            print(f"Found {len(match_list)} matches -->")
            
            for task in match_list:
                print(f"{task['id']}. {task['title']}")
        else:
            print("No match found !")

    else:
        print("Nothing to Search!")