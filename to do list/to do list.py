def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!") 
    
def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['task']} - {status}")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)  # Display tasks with indices
    try:
        index = int(input("Enter task index to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task '{tasks[index]['task']}' marked as done.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['task']},{task['done']}\n")

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task, done = line.strip().split(",")
                tasks.append({"task": task, "done": bool(done)})
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks()  # Load tasks from file

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
