from data_manager import load_data, save_data
from utils import get_non_empty_input, get_positive_integer


def add_task():
    tasks = load_data("tasks.json")

    title = get_non_empty_input("Enter task title: ")

    task = {
        "title": title,
        "status": "Pending"
    }

    tasks.append(task)
    save_data("tasks.json", tasks)

    print("Task added successfully!")


def view_tasks():
    tasks = load_data("tasks.json")

    if not tasks:
        print("No tasks found.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['status']}")

    print("===============================\n")


def complete_task():
    tasks = load_data("tasks.json")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    task_number = get_positive_integer("Enter task number to complete: ")

    if task_number > len(tasks):
        print("Invalid task number.")
        return

    tasks[task_number - 1]["status"] = "Completed"

    save_data("tasks.json", tasks)

    print("Task marked as completed!")


def delete_task():
    tasks = load_data("tasks.json")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    task_number = get_positive_integer("Enter task number to delete: ")

    if task_number > len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(task_number - 1)

    save_data("tasks.json", tasks)

    print(f"Task '{deleted_task['title']}' deleted successfully!")


def task_menu():
    while True:
        print("\n========== TASK MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")