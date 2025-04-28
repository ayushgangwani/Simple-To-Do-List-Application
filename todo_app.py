tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        # File nahi mila, to kuch nahi karna (first time run hoga to)
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No task to show\n")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

def delete_task():
    if not tasks:
        print("No task to delete\n")
        return
    
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print()
    
    try:
        task_num = int(input("Which Task you want to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks()
            print(f"Task '{removed_task}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Program start hone par pehle se tasks load karlo
load_tasks()

while True:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    print()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye! Have a productive day!")
        break
    else:
        print("Invalid choice. Please try again.\n")
