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
        print("\n\n")
        print("-"*10, "Task List", "-"*10)
        for i in task_list:
            print(f"{i['id']}. {i['title']}")
        print("\n\n")
    else:
        print("\nNo Tasks Available.")


def update_task(task_list):
    if task_list:      
        try:
            task_id = int(input("Enter the task id to update: "))
        except ValueError:
            print("\nEnter a valid Integer.\n")
            return None

        
        if 1 <= task_id <= len(task_list):
            task_title = input("Enter the Title of the task.\n>").strip()
        else:
            print("ID do not exist!")
            return None

        if task_title:
            task_list[task_id-1]["title"] = task_title
            store_data(task_list)
            print("Task updated Successfully\n")
        else:
            print("\nTask cannot be empty!\n")
            return None
            


def delete_task(task_list):
    if task_list:      
        try:
            task_id = int(input("Enter the task id to be deleted: "))
        except ValueError:
            print("\nEnter a valid Integer.\n")
            return None
        
        if 1 <= task_id <= len(task_list):
            task_list.pop(task_id-1)
            for i in range(len(task_list)):
                task_list[i]["id"] = i+1
            store_data(task_list)
            print("\nTask Deleted successfully.")
        else:
            print("\nInvalid task id.\n")
            return None     
    else:
        print("\nNothing to Delete.")