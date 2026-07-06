from src.storage import store_data

def add_task(task_list):

    task_title = input("Enter the Title of the task.\n>").strip()

    task = {
        "id" : len(task_list) + 1,
        "title" : task_title
    }
    if task_title:
        task_list.append(task)
        store_data(task_list)
        print("Task added Successfully\n")
    else:
        print("\nTask cannot be empty!\n")

def view_task(task_list):
    if task_list:
        for i in range(len(task_list)):
            print(f"{i['id']}\n{i['title']}")
    else:
        print("\nNo Tasks Available.")

def delete_task(task_list):
    if task_list:      
        try:
            task_id = int(input("Enter the task id to be deleted: "))
        except ValueError:
            print("\nEnter a valid Integer.\n")
            return None
        
        if 1 <= task_id <= len(task_list):
            task_list.pop(task_id-1)
            store_data(task_list)
            print("\nTask Deleted successfully.")
        else:
            print("\nInvalid task id.\n")
            return None     
    else:
        print("\nNothing to Delete.")